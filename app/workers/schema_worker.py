"""
Worker thread that asynchronously fetches the tables and columns of a database.
"""

from app.workers.base_worker import BaseWorker

class SchemaWorker(BaseWorker):
    def run(self):
        pass
