"""
Base QRunnable worker thread providing standard signals like result, error, progress, and finished.
"""

from PySide6.QtCore import QRunnable, QObject, Signal

class WorkerSignals(QObject):
    result = Signal(object)
    error = Signal(str)
    progress = Signal(int)
    finished = Signal()

class BaseWorker(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = WorkerSignals()
