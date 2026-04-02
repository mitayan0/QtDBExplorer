import os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QObject
from PySide6.QtWidgets import QMainWindow, QWidget

def load_ui(ui_file_path, base_instance):
    """
    Loads a .ui file and maps its children to base_instance.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    ui_abs_path = os.path.join(current_dir, "..", "ui", ui_file_path)
    
    file = QFile(ui_abs_path)
    if not file.open(QFile.ReadOnly):
        raise IOError(f"Cannot open UI file: {ui_abs_path}")
    
    loader = QUiLoader()
    # Loading as a child of base_instance
    ui = loader.load(file, base_instance)
    file.close()
    
    if not ui:
        raise RuntimeError(f"Failed to load UI: {ui_abs_path}")
        
    # Keep the reference to 'ui' to prevent garbage collection
    base_instance._ui_ref = ui
    
    # Map all children of 'ui' to 'base_instance'
    for child in ui.findChildren(QObject):
        name = child.objectName()
        if name:
            setattr(base_instance, name, child)
            
    # For QMainWindow, we need to handle special cases if the loaded UI is a QMainWindow
    if isinstance(base_instance, QMainWindow):
        # Only set the central widget if it exists and is different
        if hasattr(ui, "centralwidget"):
            base_instance.setCentralWidget(ui.centralwidget)
            
    return ui
