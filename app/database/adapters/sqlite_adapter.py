"""
Adapter to connect to SQLite databases locally.
"""

from app.database.base import BaseAdapter

class SqliteAdapter(BaseAdapter):
    def connect(self):
        pass
    def execute(self, query):
        pass
    def schema(self):
        pass
    def close(self):
        pass
