"""
Worker thread that asynchronously streams large database results into CSV or Excel files.
"""

from app.workers.base_worker import BaseWorker

class ExportWorker(BaseWorker):
    def run(self):
        pass
