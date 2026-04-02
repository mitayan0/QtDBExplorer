"""
Adapter for querying the ServiceNow REST Table API as if it were a database.
"""

from app.database.base import BaseAdapter

class ServiceNowAdapter(BaseAdapter):
    def connect(self):
        pass
    def execute(self, query):
        pass
    def schema(self):
        pass
    def close(self):
        pass
