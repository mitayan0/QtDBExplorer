
import logging
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt

logger = logging.getLogger(__name__)

class SidebarTreeHandler:
    def __init__(self, app):
        self.app = app
        # Note: the model is now owned/created by the app instance as self.app.hierarchy_model
        
    def load_tree(self, expand_group_id=None):
        """Populates the sidebar tree from the hierarchy database with state preservation."""
        logger.info("Loading connection tree...")
        
        # Preservation of expanded states
        expanded_names = set()
        if self.app.hierarchy_model:
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
        
        # 1. Fetch Connection Types
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

        # 2. Fetch Groups and associate them with types
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

        # 3. Fetch Connections and place them under groups
        conns = self.app.hierarchy.get_available_connections()
        self.app.connections_data = {c['name']: dict(c) for c in conns if c['name']}
        
        for conn_row in conns:
            conn = dict(conn_row)
            full_name = conn['name']
            if not full_name: 
                continue
            
            type_name = conn.get('raw_type')
            group_name = conn.get('raw_group')
            display_text = conn.get('short_name') or conn.get('raw_conn') or full_name
            
            if type_name in types:
                groups = types[type_name]["groups"]
                if group_name in groups:
                    conn_item = QStandardItem(display_text)
                    conn_item.setData(full_name, Qt.ItemDataRole.UserRole)
                    conn_item.setEditable(False)
                    groups[group_name]["item"].appendRow(conn_item)

        # Restore expanded states
        for i in range(self.app.hierarchy_model.rowCount()):
            type_item = self.app.hierarchy_model.item(i)
            if type_item.text() in expanded_names:
                self.app.ui.treeView.setExpanded(type_item.index(), True)
                for j in range(type_item.rowCount()):
                    group_item = type_item.child(j)
                    if group_item and f"{type_item.text()}:{group_item.text()}" in expanded_names:
                        self.app.ui.treeView.setExpanded(group_item.index(), True)
        
        logger.info("Connection tree load complete.")
