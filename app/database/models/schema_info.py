"""
Dataclass representing the schema mapping of a database (tables, columns, types).
"""

from dataclasses import dataclass, field

@dataclass
class SchemaInfo:
    tables: list = field(default_factory=list)
    columns: list = field(default_factory=list)
    types: list = field(default_factory=list)
