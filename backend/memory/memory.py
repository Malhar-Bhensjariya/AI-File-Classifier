import sqlite3
import json
from datetime import datetime

class MemoryManager:
    def __init__(self, db_path="memory/context_store.db"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self._setup()

    def _setup(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source TEXT,
                format TEXT,
                intent TEXT,
                timestamp TEXT,
                data TEXT
            )
        """)
        self.conn.commit()

    def log_metadata(self, source, format, intent):
        self.conn.execute("""
            INSERT INTO memory (source, format, intent, timestamp)
            VALUES (?, ?, ?, ?)
        """, (source, format, intent, datetime.now().isoformat()))
        self.conn.commit()

    def store_data(self, source, data):
        self.conn.execute("""
            UPDATE memory SET data = ? WHERE source = ? ORDER BY id DESC LIMIT 1
        """, (json.dumps(data), source))
        self.conn.commit()
