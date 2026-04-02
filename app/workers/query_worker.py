"""
Worker thread that asynchronously runs SQL or REST queries and returns results.
"""

from app.workers.base_worker import BaseWorker

class QueryWorker(BaseWorker):
    def run(self):
        pass
