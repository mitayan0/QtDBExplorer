"""
Contains all custom PyQt/PySide signals to allow communication between background threads and the UI.
"""

from PySide6.QtCore import QObject, Signal

class AppSignals(QObject):
    connection_added = Signal(object)
    query_executed = Signal(object)
