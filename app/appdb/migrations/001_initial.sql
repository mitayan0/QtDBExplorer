CREATE TABLE IF NOT EXISTS usf_connection_types (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	code TEXT,
	name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS usf_connection_groups (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	connection_type_id INTEGER,
	FOREIGN KEY(connection_type_id) REFERENCES usf_connection_types(id)
);

CREATE TABLE IF NOT EXISTS usf_connections (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	short_name TEXT,
	connection_group_id INTEGER,
	host TEXT,
	database TEXT,
	user TEXT,
	password NUMERIC,
	port INTEGER,
	dsn TEXT,
	db_path TEXT,
	db_file_name TEXT,
	connection_type TEXT,
	usage_count INTEGER NOT NULL DEFAULT 0,
	instance_url TEXT,
	FOREIGN KEY(connection_group_id) REFERENCES usf_connection_groups(id)
);

CREATE TABLE IF NOT EXISTS usf_processes (
    pid TEXT PRIMARY KEY,
    type TEXT,
    status TEXT,
    server TEXT,
    object TEXT,
    time_taken REAL,
    start_time TEXT,
    end_time TEXT,
    details TEXT
);

CREATE TABLE IF NOT EXISTS usf_query_history (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	query_text TEXT NOT NULL,
	timestamp TEXT NOT NULL,
	status TEXT NOT NULL DEFAULT 'Success',
	rows_affected INTEGER,
	execution_time_sec REAL,
	connection_id INTEGER NOT NULL DEFAULT -1
);