"""
Adapter that allows treating CSV files like a virtual database table using pandas or sqlite memory.
"""

from app.database.base import BaseAdapter

class CSVAdapter(BaseAdapter):
    def connect(self):
        pass
    def execute(self, query):
        pass
    def schema(self):
        pass
    def close(self):
        pass
