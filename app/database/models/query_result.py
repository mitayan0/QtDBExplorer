"""
Dataclass representing the result of a database query (columns, rows, duration, count).
"""

from dataclasses import dataclass, field

@dataclass
class QueryResult:
    columns: list = field(default_factory=list)
    rows: list = field(default_factory=list)
    duration_ms: int = 0
    row_count: int = 0
