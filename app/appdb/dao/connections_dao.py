"""
Data Access Object for safely inserting and retrieving Connection profiles from the local database.
"""

import logging
from typing import List, Optional
from app.appdb.setup import get_connection
from app.database.models.connection_profile import ConnectionProfile
from app.utils.crypto import encrypt_password, decrypt_password

logger = logging.getLogger(__name__)

class ConnectionsDAO:
    @staticmethod
    def get_all() -> List[ConnectionProfile]:
        profiles = []
        try:
            conn = get_connection()
            with conn:
                cursor = conn.execute("SELECT * FROM usf_connections ORDER BY name COLLATE NOCASE ASC")
                for row in cursor.fetchall():
                    profiles.append(ConnectionsDAO._row_to_profile(row))
            return profiles
        except Exception as e:
            logger.error(f"Failed to fetch connections: {e}")
            return []
            
    @staticmethod
    def get_by_id(profile_id: int) -> Optional[ConnectionProfile]:
        try:
            conn = get_connection()
            with conn:
                cursor = conn.execute("SELECT * FROM usf_connections WHERE id = ?", (profile_id,))
                row = cursor.fetchone()
                if row:
                    return ConnectionsDAO._row_to_profile(row)
            return None
        except Exception as e:
            logger.error(f"Failed to fetch connection {profile_id}: {e}")
            return None

    @staticmethod
    def save(profile: ConnectionProfile):
        try:
            conn = get_connection()
            encrypted_pw = encrypt_password(profile.password) if profile.password else ""
            
            with conn:
                if profile.id is not None:
                    # Update
                    conn.execute("""
                        UPDATE usf_connections 
                        SET name=?, short_name=?, connection_group_id=?, host=?, database=?, 
                            user=?, password=?, port=?, dsn=?, db_path=?, 
                            db_file_name=?, connection_type=?, usage_count=?, instance_url=?
                        WHERE id=?
                    """, (
                        profile.name, profile.short_name, profile.connection_group_id, 
                        profile.host, profile.database, profile.user, encrypted_pw, 
                        profile.port, profile.dsn, profile.db_path, profile.db_file_name, 
                        profile.connection_type, profile.usage_count, profile.instance_url, 
                        profile.id
                    ))
                else:
                    # Insert
                    cursor = conn.execute("""
                        INSERT INTO usf_connections (
                            name, short_name, connection_group_id, host, database, 
                            user, password, port, dsn, db_path, 
                            db_file_name, connection_type, usage_count, instance_url
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        profile.name, profile.short_name, profile.connection_group_id, 
                        profile.host, profile.database, profile.user, encrypted_pw, 
                        profile.port, profile.dsn, profile.db_path, profile.db_file_name, 
                        profile.connection_type, profile.usage_count, profile.instance_url
                    ))
                    profile.id = cursor.lastrowid
                    
        except Exception as e:
            logger.error(f"Failed to save connection {profile.id}: {e}")
            raise

    @staticmethod
    def delete(profile_id: int):
        try:
            conn = get_connection()
            with conn:
                conn.execute("DELETE FROM usf_connections WHERE id = ?", (profile_id,))
        except Exception as e:
            logger.error(f"Failed to delete connection {profile_id}: {e}")
            raise
            
    @staticmethod
    def _row_to_profile(row) -> ConnectionProfile:
        decrypted_pw = decrypt_password(row['password']) if row['password'] else ""
        return ConnectionProfile(
            id=row['id'],
            name=row['name'],
            short_name=row['short_name'],
            connection_group_id=row['connection_group_id'],
            host=row['host'],
            database=row['database'],
            user=row['user'],
            password=decrypted_pw,
            port=row['port'],
            dsn=row['dsn'],
            db_path=row['db_path'],
            db_file_name=row['db_file_name'],
            connection_type=row['connection_type'],
            usage_count=row['usage_count'],
            instance_url=row['instance_url']
        )
