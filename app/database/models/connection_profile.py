"""
Data models mapping perfectly to our robust usf_connections schema locally.
"""

from dataclasses import dataclass, field
from typing import Optional

@dataclass
class ConnectionProfile:
    id: Optional[int] = None
    name: str = "New Connection"
    short_name: Optional[str] = None
    connection_group_id: Optional[int] = None
    host: Optional[str] = ""
    database: Optional[str] = ""
    user: Optional[str] = ""
    password: Optional[str] = ""
    port: Optional[int] = None
    dsn: Optional[str] = ""
    db_path: Optional[str] = ""
    db_file_name: Optional[str] = ""
    connection_type: Optional[str] = ""
    usage_count: int = 0
    instance_url: Optional[str] = ""

    def get_password(self) -> str:
        """Helper to get the password plaintext gracefully."""
        return self.password or ""

    def set_password(self, plaintext: str):
        self.password = plaintext
