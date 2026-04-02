"""
Abstract Base Adapter. Defines the blueprint for connecting, executing queries, and fetching schemas.
"""

import abc

class BaseAdapter(abc.ABC):
    @abc.abstractmethod
    def connect(self):
        pass
    @abc.abstractmethod
    def execute(self, query):
        pass
    @abc.abstractmethod
    def schema(self):
        pass
    @abc.abstractmethod
    def close(self):
        pass
