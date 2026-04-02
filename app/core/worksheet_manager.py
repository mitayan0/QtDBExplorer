import os
import logging
from PySide6 import QtWidgets
from app.database.db_manager import DatabaseManager
from app.widgets.worksheet_widget import WorksheetWidget

logger = logging.getLogger(__name__)

class WorksheetManager:
    def __init__(self, app):
        self.app = app

    def add_new_worksheet(self):
        """Adds a new worksheet tab with its own independent database context."""
        logger.info("Adding a new worksheet tab...")
        
        # Create new Worksheet DB manager
        db_for_tab = DatabaseManager()

        # Create the custom worksheet widget
        ws_widget = WorksheetWidget(self.app, db_for_tab)
        
        # Populate its combo
        names = list(self.app.connections_data.keys())
        if not names: 
            names = ["sqlite", "postgres"]
        ws_widget.combo.addItems(names)
        
        # Connect signals
        # Note: These depend on app.query_handler which might not exist yet
        if hasattr(self.app, 'query_handler'):
            ws_widget.btn_exec.clicked.connect(lambda: self.app.query_handler.execute_query(ws_widget.btn_exec))
            ws_widget.btn_cancel.clicked.connect(lambda: self.app.query_handler.cancel_query(ws_widget.btn_cancel))
        
        # Connect combo signal
        # We manually disconnect to avoid multiple connections if it was already connected
        try:
            ws_widget.combo.currentTextChanged.disconnect()
        except Exception:
            pass
            
        ws_widget.combo.currentTextChanged.connect(lambda t: self.app.handle_connection_switch(t, db_for_tab, silent=False))

        # Track mappings in the main app structure
        self.app.dynamic_dbs[ws_widget.btn_exec] = db_for_tab
        self.app.dynamic_editors[ws_widget.btn_exec] = ws_widget.editor
        self.app.dynamic_combos[ws_widget.btn_exec] = ws_widget.combo
        self.app.dynamic_tables[ws_widget.btn_exec] = ws_widget.table
        self.app.dynamic_messages[ws_widget.btn_exec] = ws_widget.message_edit
        self.app.dynamic_output_tabs[ws_widget.btn_exec] = ws_widget.results_tabs
        
        # Add to TabWidget
        tab_name = f"worksheet{self.app.ui.tabWidget.count() + 1}"
        self.app.ui.tabWidget.addTab(ws_widget, tab_name)
        self.app.ui.tabWidget.setCurrentWidget(ws_widget)
        
        # Initial connection for the new tab - use whatever the combo currently shows, but SILENTLY
        self.app.handle_connection_switch(ws_widget.combo.currentText(), db_for_tab, silent=True)
        
        logger.info(f"New worksheet {tab_name} added successfully.")

    def refresh_all_combos(self):
        """Refreshes the connection list in all open worksheet tabs."""
        names = list(self.app.connections_data.keys())
        if not names: 
            names = ["sqlite", "postgres"]
            
        for i in range(self.app.ui.tabWidget.count()):
            ws_widget = self.app.ui.tabWidget.widget(i)
            if hasattr(ws_widget, 'combo'):
                current = ws_widget.combo.currentText()
                ws_widget.combo.blockSignals(True)
                ws_widget.combo.clear()
                ws_widget.combo.addItems(names)
                # Restore current if it still exists
                if current in names:
                    ws_widget.combo.setCurrentText(current)
                ws_widget.combo.blockSignals(False)
        logger.info("All connection comboboxes refreshed.")

    def remove_worksheet(self, index):
        """Removes a worksheet and renumbers remaining ones."""
        if self.app.ui.tabWidget.count() > 1:
            self.app.ui.tabWidget.removeTab(index)
            self.renumber_worksheets()
            logger.info(f"Worksheet removed at index {index}.")

    def renumber_worksheets(self):
        """Standardizes worksheet names across all tabs."""
        for i in range(self.app.ui.tabWidget.count()):
            self.app.ui.tabWidget.setTabText(i, f"worksheet{i + 1}")
