from PySide6 import QtWidgets
from app.ui.dialogs.new_psql_connection_ui import Ui_Dialog as Ui_PSQLDialog
from app.database.db_manager import DatabaseManager

class NewPSQLConnectionDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PSQLDialog()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.reject)
        self.ui.pushButton_3.clicked.connect(self.accept)
        self.ui.pushButton.clicked.connect(self.test_connection)
    
    def test_connection(self):
        host = self.ui.lineEdit.text()
        user = self.ui.lineEdit_2.text()
        db = self.ui.lineEdit_4.text()
        pwd = self.ui.lineEdit_3.text()
        port = self.ui.lineEdit_7.text() or 5432
        
        db_m = DatabaseManager()
        success, msg = db_m.connect_postgres(host, db, user, pwd, port)
        if success:
            QtWidgets.QMessageBox.information(self, "Success", "Connection test successful!")
        else:
            QtWidgets.QMessageBox.critical(self, "Error", f"Connection test failed: {msg}")
    
    def get_data(self):
        return {
            'conn_name': self.ui.lineEdit_5.text(),
            'short_name': self.ui.lineEdit_6.text(),
            'host': self.ui.lineEdit.text(),
            'user': self.ui.lineEdit_2.text(),
            'database': self.ui.lineEdit_4.text(),
            'password': self.ui.lineEdit_3.text(),
            'port': self.ui.lineEdit_7.text()
        }
