"""
Provides helper functions designed to validate user input before processing.
Examples: Ensuring a port number is valid, checking if a host IP matches correct formats, 
or ensuring an uploaded SQLite database file actually exists.
"""

def is_valid_port(port_str: str) -> bool:
    """Returns True if the port string is a valid network port (1-65535)."""
    if not port_str.isdigit():
        return False
    port = int(port_str)
    return 1 <= port <= 65535
