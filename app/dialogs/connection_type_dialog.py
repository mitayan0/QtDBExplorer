from PySide6.QtWidgets import QDialog
from app.ui.dialogs.connection_type_dialog_ui import Ui_DialogTitle

class ConnectionTypeDialog(QDialog, Ui_DialogTitle):
    def __init__(self, current_name="", parent=None):
        super().__init__(parent)
        self.setupUi(self)
        if current_name:
            self.lineEdit.setText(current_name)
        
        # Connect buttons
        self.pushButton.clicked.connect(self.accept)
        self.pushButton_2.clicked.connect(self.reject)
        
    def get_data(self):
        """Returns the name entered in the name field."""
        return self.lineEdit.text()
