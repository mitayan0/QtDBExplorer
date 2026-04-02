from PySide6.QtWidgets import QDialog
from app.ui.dialogs.new_connection_group_ui import Ui_Dialog as NewGroupUi
from app.ui.dialogs.edit_group_ui import Ui_Dialog as EditGroupUi
from app.ui.dialogs.delete_group_ui import Ui_Dialog as DeleteGroupUi
from app.ui.dialogs.delete_type_ui import Ui_Dialog as DeleteTypeUi

class NewConnectionGroupDialog(QDialog, NewGroupUi):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # Verify: pushButton_2 is 'Create', pushButton is 'Cancel'
        self.pushButton_2.clicked.connect(self.accept)
        self.pushButton.clicked.connect(self.reject)
    def get_group_name(self): return self.lineEdit.text()

class EditConnectionGroupDialog(QDialog, EditGroupUi):
    def __init__(self, current_name, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.lineEdit.setText(current_name)
        # Verify: pushButton_2 is 'Update', pushButton is 'Cancel'
        self.pushButton_2.clicked.connect(self.accept)
        self.pushButton.clicked.connect(self.reject)
    def get_new_name(self): return self.lineEdit.text()

class DeleteConnectionGroupDialog(QDialog, DeleteGroupUi):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # Verify: pushButton is 'Yes', pushButton_2 is 'No'
        self.pushButton.clicked.connect(self.accept)
        self.pushButton_2.clicked.connect(self.reject)

class DeleteConnectionTypeDialog(QDialog, DeleteTypeUi):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # Verify: pushButton is 'Yes', pushButton_2 is 'No'
        self.pushButton.clicked.connect(self.accept)
        self.pushButton_2.clicked.connect(self.reject)
