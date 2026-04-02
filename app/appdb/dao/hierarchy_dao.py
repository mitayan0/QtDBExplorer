"""
Direct SQLite implementation of hierarchy data fetching as per your specific logic.
"""

import os
import sqlite3 as sqlite
from pathlib import Path

# Resolve absolute path to the hierarchy.db in the data folder
# dao/ -> appdb/ -> app/ -> root/ (4 levels up)
ROOT_DIR = Path(__file__).parent.parent.parent.parent
DB_FILE = str(ROOT_DIR / "data" / "hierarchy.db")

def get_hierarchy_data():
    """Returns all usf_connection_types, usf_connection_groups, and usf_connections for the main tree view."""
    if not os.path.exists(DB_FILE):
        return []
        
    with sqlite.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute("SELECT id, code, name FROM usf_connection_types")
        usf_connection_types = c.fetchall()

        data = []
        for connection_type_id, code, connection_type_name in usf_connection_types:
            connection_type_data = {
                "id": connection_type_id,
                "code": code,
                "name": connection_type_name,
                "usf_connection_groups": [],
            }
            c.execute(
                "SELECT id, name FROM usf_connection_groups WHERE connection_type_id=?",
                (connection_type_id,),
            )
            connection_groups = c.fetchall()

            for connection_group_id, connection_group_name in connection_groups:
                connection_group_data = {
                    "id": connection_group_id,
                    "name": connection_group_name,
                    "usf_connections": [],
                }
                c.execute(
                    'SELECT id, name, short_name, host, "database", "user", password, port, dsn, db_path, instance_url '
                    "FROM usf_connections WHERE connection_group_id=?",
                    (connection_group_id,),
                )
                usf_connections = c.fetchall()
                for conn_row in usf_connections:
                    (
                        connection_id,
                        name,
                        short_name,
                        host,
                        db,
                        user,
                        pwd,
                        port,
                        dsn,
                        db_path,
                        instance_url,
                    ) = conn_row
                    conn_data = {
                        "id": connection_id,
                        "name": name,
                        "short_name": short_name,
                        "host": host,
                        "database": db,
                        "user": user,
                        "password": pwd,
                        "port": port,
                        "dsn": dsn,
                        "db_path": db_path,
                        "instance_url": instance_url,
                    }
                    connection_group_data["usf_connections"].append(conn_data)
                connection_type_data["usf_connection_groups"].append(
                    connection_group_data
                )
            data.append(connection_type_data)
    return data


def get_all_connections():
    """Returns a flat list of all connections with their full data."""
    if not os.path.exists(DB_FILE):
        return []

    with sqlite.connect(DB_FILE) as conn:
        c = conn.cursor()
        c.execute(
            'SELECT id, name, short_name, host, "database", "user", password, port, dsn, db_path, instance_url '
            "FROM usf_connections"
        )
        connections = []
        for row in c.fetchall():
            (
                conn_id,
                name,
                short_name,
                host,
                db,
                user,
                pwd,
                port,
                dsn,
                db_path,
                instance_url,
            ) = row
            connections.append(
                {
                    "id": conn_id,
                    "name": name,
                    "short_name": short_name,
                    "host": host,
                    "database": db,
                    "user": user,
                    "password": pwd,
                    "port": port,
                    "dsn": dsn,
                    "db_path": db_path,
                    "instance_url": instance_url,
                }
            )
    return connections
