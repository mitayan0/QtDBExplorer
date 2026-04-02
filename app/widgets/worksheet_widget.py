from PySide6 import QtWidgets, QtCore

class WorksheetWidget(QtWidgets.QWidget):
    def __init__(self, parent_window, db):
        super().__init__()
        self.parent_window = parent_window
        self.db = db
        
        # Main Layout
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        
        # 1. Connection Combobox
        self.combo = QtWidgets.QComboBox()
        self.layout.addWidget(self.combo, 0, 0, 1, 1)
        
        # 2. Toolbar Buttons
        self.toolbar = QtWidgets.QWidget()
        self.toolbar_layout = QtWidgets.QHBoxLayout(self.toolbar)
        self.toolbar_layout.setContentsMargins(0, 0, 0, 0)
        
        self.btn_exec = QtWidgets.QPushButton("execute")
        self.btn_cancel = QtWidgets.QPushButton("cancel")
        self.btn_save = QtWidgets.QPushButton("save")
        self.btn_open = QtWidgets.QPushButton("open_file")
        self.btn_limit = QtWidgets.QToolButton()
        self.btn_limit.setText("Limit")
        self.btn_analyze = QtWidgets.QToolButton()
        self.btn_analyze.setText("Explain Analyze")
        self.btn_new_ws = QtWidgets.QPushButton("new_worksheet")
        
        self.toolbar_layout.addWidget(self.btn_exec)
        self.toolbar_layout.addWidget(self.btn_cancel)
        self.toolbar_layout.addWidget(self.btn_save)
        self.toolbar_layout.addWidget(self.btn_open)
        self.toolbar_layout.addWidget(self.btn_limit)
        self.toolbar_layout.addWidget(self.btn_analyze)
        self.toolbar_layout.addWidget(self.btn_new_ws)
        self.toolbar_layout.addStretch()
        
        self.layout.addWidget(self.toolbar, 1, 0, 1, 1)
        
        # --- Top: Editor Tabs ---
        self.editor_tabs = QtWidgets.QTabWidget()
        
        # Query Editor Tab
        self.tab_editor = QtWidgets.QWidget()
        self.editor_layout = QtWidgets.QVBoxLayout(self.tab_editor)
        self.editor_layout.setContentsMargins(0, 0, 0, 0)
        self.editor = QtWidgets.QPlainTextEdit()
        self.editor_layout.addWidget(self.editor)
        self.editor_tabs.addTab(self.tab_editor, "Query_Editor")
        
        # History Tab
        self.tab_history = QtWidgets.QWidget()
        self.history_layout = QtWidgets.QVBoxLayout(self.tab_history)
        self.history_layout.setContentsMargins(0, 0, 0, 0)
        
        self.history_splitter = QtWidgets.QSplitter(QtCore.Qt.Orientation.Horizontal)
        self.history_tree = QtWidgets.QTreeView()
        self.history_tree.setMaximumWidth(250)
        
        self.history_details = QtWidgets.QGroupBox("Query_Details")
        self.details_layout = QtWidgets.QVBoxLayout(self.history_details)
        self.details_edit = QtWidgets.QTextEdit()
        self.details_layout.addWidget(self.details_edit)
        
        self.btn_panel = QtWidgets.QHBoxLayout()
        self.btn_copy = QtWidgets.QPushButton("Copy")
        self.btn_copy_editor = QtWidgets.QPushButton("Copy to Editor")
        self.btn_remove = QtWidgets.QPushButton("Remove")
        self.btn_remove_all = QtWidgets.QPushButton("Remove all")
        self.btn_panel.addWidget(self.btn_copy)
        self.btn_panel.addWidget(self.btn_copy_editor)
        self.btn_panel.addWidget(self.btn_remove)
        self.btn_panel.addWidget(self.btn_remove_all)
        self.details_layout.addLayout(self.btn_panel)
        
        self.history_splitter.addWidget(self.history_tree)
        self.history_splitter.addWidget(self.history_details)
        self.history_layout.addWidget(self.history_splitter)
        self.editor_tabs.addTab(self.tab_history, "History")
        
        # Use UI's existing results tabs from the main window (Shared results design)
        self.results_tabs = self.parent_window.ui.tabWidget_2
        self.table = self.parent_window.ui.tableView
        self.message_edit = self.parent_window.ui.plainTextEdit_3
        self.notification_edit = self.parent_window.ui.plainTextEdit_4
        
        # Add editor_tabs directly to main layout
        self.layout.addWidget(self.editor_tabs, 2, 0, 1, 1)

        # Initial signal setup
        if parent_window:
            if hasattr(self.parent_window, 'worksheet_manager'):
                self.btn_new_ws.clicked.connect(self.parent_window.worksheet_manager.add_new_worksheet)
            if hasattr(self.parent_window, 'handle_connection_switch'):
                self.combo.currentTextChanged.connect(lambda t: self.parent_window.handle_connection_switch(t, self.db))
