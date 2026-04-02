import os
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtGui import QStandardItemModel
from app.ui.main_window_ui import Ui_MainWindow
from app.core.explorer_manager import ExplorerManager
from app.core.worksheet_manager import WorksheetManager
from app.database.dao.hierarchy_dao import HierarchyDAO

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Setup the UI using the compiled class
        self.setupUi(self)
        
        # Add attributes expected by SidebarTreeHandler and ExplorerManager
        self.ui = self
        self.hierarchy = HierarchyDAO()
        self.hierarchy_model = QStandardItemModel()
        self.connections_data = {}
        
        # New worksheet-related dictionaries for independent tab management
        self.dynamic_dbs = {}
        self.dynamic_editors = {}
        self.dynamic_combos = {}
        self.dynamic_tables = {}
        self.dynamic_messages = {}
        self.dynamic_output_tabs = {}
        
        # Initialize the managers
        self.worksheet_manager = WorksheetManager(self)
        self.explorer = ExplorerManager(self)
        
        # Set the model to the treeView
        self.treeView.setModel(self.hierarchy_model)
        
        # Setup explore sidebar and initial tab
        self.explorer.setup_sidebar_trees()
        self.explorer.load_connections_hierarchy()
        
        # Clear default tabs and add a new one properly managed by WorksheetManager
        while self.ui.tabWidget.count() > 0:
            self.ui.tabWidget.removeTab(0)
        self.worksheet_manager.add_new_worksheet()
        
        # Connect tab close
        self.ui.tabWidget.tabCloseRequested.connect(self.worksheet_manager.remove_worksheet)
        
        # Additional setup
        self.setWindowTitle("QtDBExplorer - Developer Edition")

    def get_active_worksheet_widget(self):
        """Returns the currently active worksheet object from the UI."""
        return self.ui.tabWidget.currentWidget()

    def handle_connection_switch(self, conn_name, db_manager, silent=False):
        """Switches the database connection for a specific worksheet tab."""
        if not conn_name: 
            return

        conn_info = self.connections_data.get(conn_name)
        if not conn_info:
            return

        db_type = (conn_info.get('type') or "").lower()
        success, msg = False, ""
        
        if "postgres" in db_type:
            success, msg = db_manager.connect_postgres(
                conn_info.get('host'), conn_info.get('database'), conn_info.get('user'),
                conn_info.get('password'), conn_info.get('port') or 5432, conn_name=conn_name
            )
        else:
            # Default to SQLite for local file paths
            db_path = conn_info.get('db_path') or os.path.join("data", "hierarchy.db")
            success, msg = db_manager.connect(db_path, conn_name=conn_name)

        if not silent:
            if not success:
                QMessageBox.critical(self, "Connection Error", msg)
        
        # We REMOVED the successful MessageBox here
        # so the user isn't interrupted by "Connected to SQLite" every time.
