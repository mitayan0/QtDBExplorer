"""
Core application window. Owns the thread pool, central tabs, and coordinates docking panels.
"""

from PySide6.QtWidgets import QMainWindow
from app.utils.ui_loader import load_ui

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # Load the UI file onto this instance
        load_ui("main_window.ui", self)
        
        # Additional setup can go here
        self.setWindowTitle("QtDBExplorer - Developer Edition")
