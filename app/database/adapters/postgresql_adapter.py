"""
Adapter to connect to PostgreSQL databases (using psycopg2 or similar).
"""

from app.database.base import BaseAdapter

class PostgresAdapter(BaseAdapter):
    def connect(self):
        pass
    def execute(self, query):
        pass
    def schema(self):
        pass
    def close(self):
        pass
