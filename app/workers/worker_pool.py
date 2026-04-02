"""
Thin wrapper around QThreadPool to manage background worker submissions centrally.
"""

from PySide6.QtCore import QThreadPool

class WorkerPool:
    @staticmethod
    def get_instance():
        return QThreadPool.globalInstance()
