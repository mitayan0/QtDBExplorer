from app.appdb.setup import get_connection, DB_PATH
import sqlite3

class HierarchyDAO:
    def __init__(self):
        self.db_file = str(DB_PATH)
        
    def get_all_connection_types(self):
        """Returns all connection types."""
        conn = get_connection()
        try:
            return conn.execute("SELECT id, name FROM usf_connection_types").fetchall()
        finally:
            conn.close()
            
    def get_all_groups_and_types(self):
        """Returns groups along with their parent type names."""
        conn = get_connection()
        try:
            query = """
                SELECT g.id as group_id, g.name as group_name, t.name as type_name
                FROM usf_connection_groups g
                JOIN usf_connection_types t ON g.connection_type_id = t.id
            """
            return conn.execute(query).fetchall()
        finally:
            conn.close()

    def get_available_connections(self):
        """Fetches available connections with hierarchical names from hierarchy.db"""
        try:
            # Using str(DB_PATH) directly
            conn = sqlite3.connect(self.db_file, check_same_thread=False)
            conn.row_factory = sqlite3.Row # Use Row factory for easier access if needed
            cur = conn.cursor()
            cur.execute("""
                SELECT 
                    c.id as conn_id,
                    COALESCE(t.name, 'None') as type_name, 
                    COALESCE(g.name, 'None') as group_name, 
                    c.name as conn_name, 
                    COALESCE(c.short_name, '') as short_name,
                    c.connection_type, 
                    c.host, 
                    c.database, 
                    c.user, 
                    c.password, 
                    c.port, 
                    c.db_path,
                    g.id as group_id,
                    t.id as type_id
                FROM usf_connections c
                LEFT JOIN usf_connection_groups g ON c.connection_group_id = g.id
                LEFT JOIN usf_connection_types t ON g.connection_type_id = t.id
            """)
            rows = cur.fetchall()
            conn.close()
            
            conns = []
            for row in rows:
                type_name = row['type_name']
                group_name = row['group_name']
                conn_name = row['conn_name']
                short_name = row['short_name']
                
                display_name = f"{type_name} -> {group_name} -> {conn_name}"
                if short_name:
                    display_name += f" ({short_name})"
                
                conns.append({
                    'name': display_name,
                    'raw_type': type_name,
                    'raw_group': group_name,
                    'raw_conn': conn_name,
                    'short_name': short_name,
                    'type': row['connection_type'],
                    'host': row['host'],
                    'database': row['database'],
                    'user': row['user'],
                    'password': row['password'],
                    'port': row['port'],
                    'db_path': row['db_path'],
                    'group_id': row['group_id'],
                    'type_id': row['type_id'],
                    'conn_id': row['conn_id']
                })
            return conns
        except Exception as e:
            print(f"Error fetching connections from DB: {e}")
            return []

    def add_connection_type(self, name, code):
        """Adds a new connection type."""
        conn = get_connection()
        try:
            with conn:
                conn.execute("INSERT INTO usf_connection_types (name, code) VALUES (?, ?)", (name, code))
            return True, f"Successfully added connection type '{name}'"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()

    def update_connection_type(self, type_id, name):
        """Updates an existing connection type."""
        conn = get_connection()
        try:
            with conn:
                conn.execute("UPDATE usf_connection_types SET name = ? WHERE id = ?", (name, type_id))
            return True, "Successfully updated connection type"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()

    def delete_connection_type(self, type_id):
        """Deletes a connection type and all its associated groups and connections."""
        conn = get_connection()
        try:
            type_id = int(type_id)
            with conn:
                # 1. Delete connections attached to groups in this type
                conn.execute("""
                    DELETE FROM usf_connections WHERE connection_group_id IN 
                    (SELECT id FROM usf_connection_groups WHERE connection_type_id = ?)
                """, (type_id,))
                
                # 2. Delete groups in this type
                conn.execute("DELETE FROM usf_connection_groups WHERE connection_type_id = ?", (type_id,))
                
                # 3. Finally, delete the type
                cursor = conn.execute("DELETE FROM usf_connection_types WHERE id = ?", (type_id,))
                
                if cursor.rowcount == 0:
                    return False, f"Connection type with ID {type_id} not found."
                    
            return True, "Successfully deleted connection type"
        except Exception as e:
            logger.error(f"Error deleting connection type {type_id}: {e}")
            return False, str(e)
        finally:
            conn.close()

    def add_connection_group(self, type_id, name):
        """Adds a new connection group."""
        conn = get_connection()
        try:
            with conn:
                conn.execute("INSERT INTO usf_connection_groups (name, connection_type_id) VALUES (?, ?)", (name, type_id))
            return True, f"Successfully added group '{name}'"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()

    def update_connection_group(self, group_id, name):
        """Updates an existing connection group."""
        conn = get_connection()
        try:
            with conn:
                conn.execute("UPDATE usf_connection_groups SET name = ? WHERE id = ?", (name, group_id))
            return True, "Successfully updated group"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()

    def delete_connection_group(self, group_id):
        """Deletes a connection group and all its associated connections."""
        conn = get_connection()
        try:
            group_id = int(group_id)
            with conn:
                # 1. Delete connections in this group
                conn.execute("DELETE FROM usf_connections WHERE connection_group_id = ?", (group_id,))
                
                # 2. Finally, delete the group
                cursor = conn.execute("DELETE FROM usf_connection_groups WHERE id = ?", (group_id,))
                
                if cursor.rowcount == 0:
                    return False, f"Group with ID {group_id} not found."
                    
            return True, "Successfully deleted group"
        except Exception as e:
            logger.error(f"Error deleting connection group {group_id}: {e}")
            return False, str(e)
        finally:
            conn.close()

    def add_new_connection(self, group_id, name, short_name, conn_type, host, db, user, password, port):
        """Adds a new database connection."""
        conn = get_connection()
        try:
            with conn:
                query = """
                    INSERT INTO usf_connections (connection_group_id, name, short_name, connection_type, host, database, user, password, port)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """
                conn.execute(query, (group_id, name, short_name, conn_type, host, db, user, password, port))
            return True, f"Successfully added connection '{name}'"
        except Exception as e:
            return False, str(e)
        finally:
            conn.close()

    def delete_connection(self, conn_id):
        """Deletes a specific database connection."""
        conn = get_connection()
        import logging
        logger = logging.getLogger(__name__)
        try:
            conn_id = int(conn_id)
            with conn:
                cursor = conn.execute("DELETE FROM usf_connections WHERE id = ?", (conn_id,))
                if cursor.rowcount == 0:
                    return False, f"Connection with ID {conn_id} not found."
            return True, "Successfully deleted connection"
        except Exception as e:
            logger.error(f"Error deleting connection {conn_id}: {e}")
            return False, str(e)
        finally:
            conn.close()

