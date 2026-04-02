"""
Global singleton used to share application state across different UI windows and workers.
"""

class AppState:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
