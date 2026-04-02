"""
Handles database initialization, directories, and executes SQL schema migrations on startup.
"""

import os
import sqlite3
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

# Resolving paths
ROOT_DIR = Path(__file__).parent.parent.parent
DATA_DIR = ROOT_DIR / "data"
DB_PATH = DATA_DIR / "appdata.db"
MIGRATIONS_DIR = Path(__file__).parent / "migrations"

def get_connection() -> sqlite3.Connection:
    """Returns a connection to the app's internal database."""
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn

def initialize():
    """Ensures data directory exists, db is created, and migrations are applied."""
    if not DATA_DIR.exists():
        logger.info(f"Creating data directory at {DATA_DIR}")
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        
    conn = get_connection()
    try:
        # Create migrations tracking table if not exists
        conn.execute('''
            CREATE TABLE IF NOT EXISTS schema_migrations (
                version TEXT PRIMARY KEY,
                applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Get applied migrations
        cursor = conn.execute("SELECT version FROM schema_migrations")
        applied_migrations = {row['version'] for row in cursor.fetchall()}
        
        # Find all .sql files in migrations dir, sort alphabetically
        migration_files = sorted([f for f in os.listdir(MIGRATIONS_DIR) if f.endswith('.sql')])
        
        for migration_file in migration_files:
            if migration_file not in applied_migrations:
                logger.info(f"Applying migration: {migration_file}")
                
                with open(MIGRATIONS_DIR / migration_file, 'r', encoding='utf-8') as f:
                    sql_script = f.read()
                    
                # Run script
                with conn:
                    conn.executescript(sql_script)
                    conn.execute("INSERT INTO schema_migrations (version) VALUES (?)", (migration_file,))
                    
                logger.info(f"Successfully applied {migration_file}")
                
    except Exception as e:
        logger.error(f"Error during appdb initialization: {e}")
        raise
    finally:
        conn.close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    initialize()
