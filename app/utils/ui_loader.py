"""
Helper used to dynamically load raw Qt .ui files and link them to python logic classes.
"""

import os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice

class UiLoader(QUiLoader):
    """Custom UI loader to permit promoting widgets if needed later."""
    def __init__(self, baseinstance, customWidgets=None):
        super(UiLoader, self).__init__(baseinstance)
        self.baseinstance = baseinstance

    def createWidget(self, className, parent=None, name=''):
        if parent is None and self.baseinstance:
            return self.baseinstance
        else:
            return super(UiLoader, self).createWidget(className, parent, name)

def load_ui(ui_file_path, base_instance=None):
    """
    Loads a .ui file onto a base instance or returns a new widget.
    Path is relative to the app/ui directory.
    """
    # Resolve absolute path to the UI file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    ui_abs_path = os.path.join(current_dir, "..", "ui", ui_file_path)
    
    file = QFile(ui_abs_path)
    if not file.open(QFile.ReadOnly):
        raise IOError(f"Cannot open UI file: {ui_abs_path}")
        
    loader = UiLoader(base_instance)
    widget = loader.load(file, base_instance)
    file.close()
    
    return widget
