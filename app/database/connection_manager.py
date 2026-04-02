"""
Manages a dictionary of active database connections (add, get, remove, test).
"""

class ConnectionManager:
    def __init__(self):
        self.connections = {}
    def add(self, id, conn):
        self.connections[id] = conn
    def get(self, id):
        return self.connections.get(id)
