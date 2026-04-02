"""
Main application entry point. Initializes the app and launches the MainWindow.
"""

import sys
import os
import logging
from PySide6.QtWidgets import QApplication
from app.appdb.setup import initialize
from app.windows.main_window import MainWindow

# Basic logging configuration for the app
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("QtDBExplorer")

class QtDBExplorerApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.app.setApplicationName("QtDBExplorer")
        
        # Initialize the internal database and directories
        initialize()
        
        # Setup the main window
        self.window = MainWindow()

    def run(self):
        self.window.show()
        return self.app.exec()

if __name__ == '__main__':
    try:
        app_instance = QtDBExplorerApp()
        sys.exit(app_instance.run())
    except Exception as e:
        logger.critical(f"Application failed to start: {e}", exc_info=True)
        sys.exit(1)
