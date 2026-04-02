"""
Adapter to connect to Oracle databases via cx_Oracle/oracledb.
"""

from app.database.base import BaseAdapter

class OracleAdapter(BaseAdapter):
    def connect(self):
        pass
    def execute(self, query):
        pass
    def schema(self):
        pass
    def close(self):
        pass
