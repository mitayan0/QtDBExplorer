import os
import logging
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QFrame, QAbstractItemView, QWidget

# Updated Imports to match project structure
from app.dialogs.connection_type_dialog import ConnectionTypeDialog
from app.dialogs.psql_connection_dialog import NewPSQLConnectionDialog
from app.dialogs.manager_dialogs import (NewConnectionGroupDialog, EditConnectionGroupDialog, 
                                     DeleteConnectionGroupDialog, DeleteConnectionTypeDialog)

logger = logging.getLogger(__name__)

class ExplorerManager:
    def __init__(self, app):
        self.app = app

    def setup_sidebar_trees(self):
        # 1. Map existing UI widgets from Designer (ui_test29.py -> main_window_ui.py)
        # Using the actual names from the .ui file seen earlier
        self.app.object_explorer_label = self.app.ui.label_2
        self.app.explorer_search_box = self.app.ui.lineEdit
        self.app.add_new_type_btn = self.app.ui.toolButton
        
        self.app.explorer_search_box.setPlaceholderText("Filter Connections...")
        self.app.explorer_search_box.setStyleSheet("""
            QLineEdit {
                border: 1px solid #A9A9A9;
                border-radius: 4px;
                padding: 2px 5px;
                background-color: #ffffff;
            }
        """)
        self.app.explorer_search_box.textChanged.connect(self.filter_object_explorer)
        
        self.app.add_new_type_btn.setToolTip("Add New Connection Type")
        self.app.add_new_type_btn.clicked.connect(self.add_connection_type_dialog)
        
        # 3. Setup Splitter if needed, but here we just use the Designer's splitter (self.app.ui.splitter)
        # Ensure the trees are styled
        self.app.ui.treeView.setFrameShape(QFrame.Shape.NoFrame)
        self.app.ui.treeView.clicked.connect(self.on_hierarchy_item_clicked)
        self.app.ui.treeView.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.app.ui.treeView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.app.ui.treeView.setHeaderHidden(True)
        self.app.ui.treeView.setIndentation(15)
        
        # Ensure hierarchy_model exists
        if not hasattr(self.app, 'hierarchy_model'):
            self.app.hierarchy_model = QStandardItemModel()
            
        self.app.ui.treeView.setModel(self.app.hierarchy_model)
        self.app.ui.treeView.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.app.ui.treeView.customContextMenuRequested.connect(self.show_explorer_context_menu)

        self.app.ui.treeView_2.setFrameShape(QFrame.Shape.NoFrame)
        self.app.schema_tree = self.app.ui.treeView_2
        self.app.schema_model = QStandardItemModel()
        self.app.schema_model.setHorizontalHeaderLabels(["Database Schema"])
        self.app.schema_tree.setModel(self.app.schema_model)
        
        self.apply_schema_header_style()
        self.app.schema_tree.doubleClicked.connect(self.on_schema_item_double_clicked)
        self.app.schema_tree.setIndentation(15)
        self.app.schema_tree.setColumnWidth(0, 250)

    def filter_object_explorer(self, text):
        """Filters the hierarchy tree based on search text"""
        for i in range(self.app.hierarchy_model.rowCount()):
            type_item = self.app.hierarchy_model.item(i)
            type_match = text.lower() in type_item.text().lower()
            
            group_visible_count = 0
            for j in range(type_item.rowCount()):
                group_item = type_item.child(j)
                group_match = text.lower() in group_item.text().lower()
                
                conn_visible_count = 0
                for k in range(group_item.rowCount()):
                    conn_item = group_item.child(k)
                    conn_match = text.lower() in conn_item.text().lower()
                    
                    is_visible = type_match or group_match or conn_match
                    self.app.ui.treeView.setRowHidden(k, group_item.index(), not is_visible)
                    if is_visible: conn_visible_count += 1
                
                group_item_visible = type_match or group_match or (conn_visible_count > 0)
                self.app.ui.treeView.setRowHidden(j, type_item.index(), not group_item_visible)
                if group_item_visible: group_visible_count += 1
            
            self.app.ui.treeView.setRowHidden(i, QModelIndex(), not (type_match or group_visible_count > 0))

    def add_connection_type_dialog(self):
        dialog = ConnectionTypeDialog(parent=self.app)
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            name = dialog.get_data()
            if not name:
                QtWidgets.QMessageBox.warning(self.app, "Validation Error", "Name is required.")
                return
            
            # Use 'GENERIC' or similar for code if not provided by dialog
            success, msg = self.app.hierarchy.add_connection_type(name, name.upper())
            if success:
                QtWidgets.QMessageBox.information(self.app, "Success", msg)
                # Note: self.app.load_connections() might not exist, using load_connections_hierarchy()
                if hasattr(self.app, 'load_connections'):
                    self.app.load_connections()
                self.load_connections_hierarchy() 
            else:
                QtWidgets.QMessageBox.critical(self.app, "Error", msg)

    def apply_schema_header_style(self):
        header = self.app.ui.treeView_2.header()
        header.setStyleSheet("""
            QHeaderView::section {
                background-color: #9099a2;
                color: white;
                padding: 4px;
                border: 1px solid #7a858e;
                font-weight: bold;
            }
        """)

    def load_connections_hierarchy(self, expand_group_id=None):
        """Populates the hierarchy tree from the DAO."""
        # Preservation of expanded states
        expanded_names = set()
        for i in range(self.app.hierarchy_model.rowCount()):
            type_item = self.app.hierarchy_model.item(i)
            if self.app.ui.treeView.isExpanded(type_item.index()):
                expanded_names.add(type_item.text())
                for j in range(type_item.rowCount()):
                    group_item = type_item.child(j)
                    if self.app.ui.treeView.isExpanded(group_item.index()):
                        expanded_names.add(f"{type_item.text()}:{group_item.text()}")

        self.app.hierarchy_model.clear()
        self.app.hierarchy_model.setHorizontalHeaderLabels(["Connection Hierarchy"])
        
        all_types = self.app.hierarchy.get_all_connection_types()
        types = {}
        for t_obj in all_types:
            tname = t_obj["name"]
            type_item = QStandardItem(tname)
            type_item.setData("type", Qt.ItemDataRole.UserRole)
            type_item.setData(t_obj["id"], Qt.ItemDataRole.UserRole + 1)
            type_item.setEditable(False)
            self.app.hierarchy_model.appendRow(type_item)
            types[tname] = {"item": type_item, "groups": {}}

        all_groups = self.app.hierarchy.get_all_groups_and_types()
        for g_obj in all_groups:
            tname = g_obj["type_name"]
            gname = g_obj["group_name"]
            gid = g_obj["group_id"]
            if tname in types:
                type_item = types[tname]["item"]
                groups = types[tname]["groups"]
                if gname not in groups:
                    group_item = QStandardItem(gname)
                    group_item.setData("group", Qt.ItemDataRole.UserRole)
                    group_item.setData(gid, Qt.ItemDataRole.UserRole + 1)
                    group_item.setEditable(False)
                    type_item.appendRow(group_item)
                    groups[gname] = {"item": group_item}
                if gid == expand_group_id:
                    expanded_names.add(tname)
                    expanded_names.add(f"{tname}:{gname}")

        conns = self.app.hierarchy.get_available_connections()
        # Ensure we store it as a dict of dicts, conn_row is sqlite3.Row
        self.app.connections_data = {c['name']: dict(c) for c in conns if c['name']}
        
        for conn_row in conns:
            conn = dict(conn_row)
            full_name = conn['name']
            if not full_name: continue
            
            # Use raw data from the dict for hierarchy mapping
            type_name = conn.get('raw_type')
            group_name = conn.get('raw_group')
            # Only show short_name in the tree, or raw_conn as fallback
            display_text = conn.get('short_name') or conn.get('raw_conn')
            
            if type_name in types:
                groups = types[type_name]["groups"]
                if group_name in groups:
                    conn_item = QStandardItem(display_text)
                    conn_item.setData(full_name, Qt.ItemDataRole.UserRole)
                    conn_item.setEditable(False)
                    groups[group_name]["item"].appendRow(conn_item)

        # Synchronize connection list with all open worksheets
        if hasattr(self.app, 'worksheet_manager'):
            self.app.worksheet_manager.refresh_all_combos()
            
        logger.info("Connection tree load complete.")

        for i in range(self.app.hierarchy_model.rowCount()):
            type_item = self.app.hierarchy_model.item(i)
            if type_item.text() in expanded_names:
                self.app.ui.treeView.setExpanded(type_item.index(), True)
                for j in range(type_item.rowCount()):
                    group_item = type_item.child(j)
                    if group_item and f"{type_item.text()}:{group_item.text()}" in expanded_names:
                        self.app.ui.treeView.setExpanded(group_item.index(), True)

    def show_explorer_context_menu(self, position):
        index = self.app.ui.treeView.indexAt(position)
        if not index.isValid(): return
        item = self.app.hierarchy_model.itemFromIndex(index)
        item_data = item.data(Qt.ItemDataRole.UserRole)
        menu = QtWidgets.QMenu()

        if item_data == "type":
            type_id = item.data(Qt.ItemDataRole.UserRole + 1)
            menu.addAction("New Group").triggered.connect(lambda t=type_id: self.open_new_group_dialog(t))
            menu.addAction("Edit Type").triggered.connect(lambda t=type_id, n=item.text(): self.open_edit_type_dialog(t, n))
            menu.addAction("Delete Type").triggered.connect(lambda t=type_id: self.open_delete_type_dialog(t))
        elif item_data == "group":
            group_id = item.data(Qt.ItemDataRole.UserRole + 1)
            parent = item.parent()
            parent_text = parent.text().lower() if parent else ""
            if "postgres" in parent_text:
                menu.addAction("New Connection").triggered.connect(lambda g=group_id: self.open_new_psql_connection_dialog(g))
            menu.addAction("Edit Group").triggered.connect(lambda g=group_id, n=item.text(): self.open_edit_group_dialog(g, n))
            menu.addAction("Delete Group").triggered.connect(lambda g=group_id: self.open_delete_group_dialog(g))
        
        menu.exec(self.app.ui.treeView.viewport().mapToGlobal(position))

    def on_hierarchy_item_clicked(self, index):
        item = self.app.hierarchy_model.itemFromIndex(index)
        data = item.data(Qt.ItemDataRole.UserRole)
        if not data or data in ["type", "group"]: return
        self.load_schema_for_connection(data)

    def load_schema_for_connection(self, full_name):
        """Loads schema into the secondary tree view."""
        # Note: self.app.get_active_worksheet_widget() might need implementation
        if not hasattr(self.app, 'get_active_worksheet_widget'):
            logger.warning("get_active_worksheet_widget not implemented on app.")
            return

        conn_info = self.app.connections_data.get(full_name)
        active_ws = self.app.get_active_worksheet_widget()
        if not conn_info or not active_ws: return

        db_type = (conn_info.get('type') or "").lower()
        success, msg = False, ""
        
        # This assumes active_ws.db is available
        if not hasattr(active_ws, 'db'):
            logger.warning("Worksheet does not have a database manager.")
            return

        if "postgres" in db_type:
            success, msg = active_ws.db.connect_postgres(
                conn_info.get('host'), conn_info.get('database'), conn_info.get('user'),
                conn_info.get('password'), conn_info.get('port') or 5432, conn_name=full_name
            )
        else:
            db_path = conn_info.get('db_path') or os.path.join("data", "hierarchy.db")
            success, msg = active_ws.db.connect(db_path, conn_name=full_name)

        if not success:
            self.app.schema_model.clear()
            self.app.schema_model.setHorizontalHeaderLabels(["Database Schema"])
            return

        self.app.schema_model.clear()
        self.app.schema_model.setHorizontalHeaderLabels(["Name", "Type"])
        try:
            schema_data = active_ws.db.get_schema()
            parent = self.app.schema_model.invisibleRootItem()
            if "postgres" in db_type:
                parent = QStandardItem("Schemas")
                self.app.schema_model.appendRow([parent, QStandardItem("Group")])
            
            nodes = {}
            for item in schema_data:
                name, otype, cols = item[0], item[1], item[2]
                sname = item[3] if len(item) > 3 else None
                curr = parent
                if sname and "postgres" in db_type:
                    if sname not in nodes:
                        nodes[sname] = QStandardItem(sname)
                        parent.appendRow([nodes[sname], QStandardItem("Schema")])
                    curr = nodes[sname]
                oitem = QStandardItem(name)
                curr.appendRow([oitem, QStandardItem(otype)])
                for cname, ctype in cols:
                    oitem.appendRow([QStandardItem(cname), QStandardItem(ctype)])
            if "postgres" in db_type:
                self.app.ui.treeView_2.expand(self.app.schema_model.indexFromItem(parent))
            self.app.ui.treeView_2.resizeColumnToContents(0)
        except Exception as e:
            logger.exception(f"Error fetching schema: {e}")

    def on_schema_item_double_clicked(self, index):
        pass

    def open_new_psql_connection_dialog(self, group_id):
        dialog = NewPSQLConnectionDialog(self.app)
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            data = dialog.get_data()
            success, msg = self.app.hierarchy.add_new_connection(
                group_id, data['conn_name'], data['short_name'], 'PostgreSQL',
                data['host'], data['database'], data['user'], data['password'], data['port']
            )
            if success:
                if hasattr(self.app, 'load_connections'):
                    self.app.load_connections()
                self.load_connections_hierarchy(expand_group_id=group_id)
            else:
                QtWidgets.QMessageBox.critical(self.app, "Error", msg)

    def open_new_group_dialog(self, type_id):
        dialog = NewConnectionGroupDialog(self.app)
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            name = dialog.get_group_name()
            if not name: return
            success, msg = self.app.hierarchy.add_connection_group(type_id, name)
            if success:
                self.load_connections_hierarchy()
                for i in range(self.app.hierarchy_model.rowCount()):
                    item = self.app.hierarchy_model.item(i)
                    if item.data(Qt.ItemDataRole.UserRole + 1) == type_id:
                        self.app.ui.treeView.setExpanded(item.index(), True)
                        break

    def open_edit_group_dialog(self, group_id, current_name):
        dialog = EditConnectionGroupDialog(current_name, self.app)
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            name = dialog.get_new_name()
            if not name: return
            success, msg = self.app.hierarchy.update_connection_group(group_id, name)
            if success: self.load_connections_hierarchy()

    def open_delete_group_dialog(self, group_id):
        dialog = DeleteConnectionGroupDialog(self.app)
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            success, msg = self.app.hierarchy.delete_connection_group(group_id)
            if success:
                QtWidgets.QMessageBox.information(self.app, "Success", msg)
                self.load_connections_hierarchy()
            else:
                QtWidgets.QMessageBox.critical(self.app, "Error", msg)

    def open_edit_type_dialog(self, type_id, current_name):
        dialog = ConnectionTypeDialog(current_name, self.app)
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            name = dialog.get_data()
            if not name: return
            success, msg = self.app.hierarchy.update_connection_type(type_id, name)
            if success: self.load_connections_hierarchy()

    def open_delete_type_dialog(self, type_id):
        dialog = DeleteConnectionTypeDialog(self.app)
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            success, msg = self.app.hierarchy.delete_connection_type(type_id)
            if success:
                QtWidgets.QMessageBox.information(self.app, "Success", msg)
                self.load_connections_hierarchy()
            else:
                QtWidgets.QMessageBox.critical(self.app, "Error", msg)
