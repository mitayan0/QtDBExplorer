import sqlite3
import os
import sys
import psycopg2
import logging

logger = logging.getLogger(__name__)

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Default to current directory if not specified
DB_FILE = resource_path(os.path.join("database", "hierarchy.db"))

class DatabaseManager:
    def __init__(self):
        self.conn = None
        self.db_type = None  # 'sqlite' or 'postgres'
        self.active_connection_name = None

    def connect(self, db_path=DB_FILE, conn_name="Default SQLite"):
        """Connects to SQLite by default"""
        try:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(db_path), exist_ok=True)
            
            self.close() # Close existing connection if any
            self.conn = sqlite3.connect(db_path, check_same_thread=False)
            self.conn.row_factory = sqlite3.Row
            self.db_type = 'sqlite'
            self.active_connection_name = conn_name
            return True, f"Connected to SQLite"
        except Exception as e:
            return False, f"Unable to open database file: {str(e)}"

    def connect_postgres(self, host, database, user, password, port=5432, conn_name=None):
        """Connects to PostgreSQL"""
        try:
            self.close() # Close existing connection if any
            self.conn = psycopg2.connect(
                host=host,
                database=database,
                user=user,
                password=password,
                port=port
            )
            self.db_type = 'postgres'
            self.active_connection_name = conn_name or f"{host}:{database}"
            return True, "PostgreSQL connected successfully!"
        except Exception as e:
            return False, f"PostgreSQL connection failed: {str(e)}"

    def get_connection(self):
        return self.conn

    def get_schema(self):
        if not self.conn:
            raise Exception("No active connection")
            
        cursor = self.conn.cursor()
        
        if self.db_type == 'sqlite':
            cursor.execute("SELECT name, type FROM sqlite_master WHERE type IN ('table', 'view') AND name NOT LIKE 'sqlite_%' ORDER BY type, name;")
            objects = cursor.fetchall()
            
            schema = []
            for obj in objects:
                obj_name = obj[0]
                obj_type = obj[1]
                cursor.execute(f"PRAGMA table_info('{obj_name}')")
                columns = cursor.fetchall()
                cols = [(col[1], col[2]) for col in columns]
                schema.append((obj_name, obj_type.capitalize(), cols))
            return schema
            
        elif self.db_type == 'postgres':
            try:
                # Get tables and views from ALL schemas except system ones
                cursor.execute("""
                    SELECT table_schema, table_name, table_type 
                    FROM information_schema.tables 
                    WHERE table_schema NOT IN ('information_schema', 'pg_catalog')
                    ORDER BY table_schema, table_type, table_name;
                """)
                objects = cursor.fetchall()
                
                schema = []
                for schema_info in objects:
                    schema_name, obj_name, obj_type = schema_info[0], schema_info[1], schema_info[2]
                    # Map 'BASE TABLE' to 'Table' and 'VIEW' to 'View'
                    type_name = 'Table' if obj_type == 'BASE TABLE' else 'View'
                    
                    # Get columns for each table
                    cursor.execute("""
                        SELECT column_name, data_type 
                        FROM information_schema.columns 
                        WHERE table_schema = %s AND table_name = %s
                        ORDER BY ordinal_position;
                    """, (schema_name, obj_name))
                    columns = cursor.fetchall()
                    # Store columns as (name, type)
                    cols = [(col[0], col[1]) for col in columns]
                    # Format: (object_name, type_name, columns, schema_name)
                    schema.append((obj_name, type_name, cols, schema_name))
                return schema
            except Exception as e:
                if self.conn:
                    self.conn.rollback()
                raise e
            
        return []

    def execute_query(self, query):
        """Executes a query and returns (is_select, rows, description) or raises Exception"""
        if not self.conn:
            raise Exception("No active connection")
            
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            
            # Check if it's a SELECT query
            if query.strip().upper().startswith("SELECT"):
                rows = cursor.fetchall()
                return True, rows, cursor.description
            else:
                if self.db_type == 'postgres':
                    self.conn.commit()
                return False, None, None
        except Exception as e:
            # If a transaction error occurs in Postgres, we MUST rollback
            if self.db_type == 'postgres' and self.conn:
                try:
                    self.conn.rollback()
                except:
                    pass
            raise e

    def cancel_query(self):
        """Attempts to cancel the currently running query"""
        if not self.conn:
            return False, "No active connection"
        
        try:
            if self.db_type == 'sqlite':
                # sqlite3 allows interrupting from another thread
                self.conn.interrupt()
                return True, "SQLite query interrupted"
            elif self.db_type == 'postgres':
                # psycopg2 connection has a cancel method
                if hasattr(self.conn, 'cancel'):
                    self.conn.cancel()
                    return True, "PostgreSQL query canceled"
            return False, "Cancellation not supported for this database type"
        except Exception as e:
            return False, f"Failed to cancel query: {str(e)}"

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            self.db_type = None
            self.active_connection_name = None
