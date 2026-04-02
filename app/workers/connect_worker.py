"""
Worker thread that asynchronously opens or tests a database connection so the UI doesn't freeze.
"""

from app.workers.base_worker import BaseWorker

class ConnectWorker(BaseWorker):
    def run(self):
        pass
