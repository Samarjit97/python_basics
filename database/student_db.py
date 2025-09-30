import sqlite3
from pathlib import Path
DB_PATH = Path(__file__).parent / "students.db"

DB_PATH = Path("../students.db")

def ensure_table(conn):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            name  TEXT NOT NULL,
            grade INTEGER NOT NULL
        );
    """)
    conn.commit()

def seed_if_empty(conn):
    """Insert a couple of rows if the table is empty."""
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM students")
    (count,) = cur.fetchone()
    if count == 0:
        cur.executemany(
            "INSERT INTO students (name, grade) VALUES (?, ?)",
            [("John", 85), ("Alice", 90), ("Maria", 78)]
        )
        conn.commit()

def fetch_students(conn):
    cur = conn.cursor()
    cur.execute("SELECT id, name, grade FROM students ORDER BY id;")
    return cur.fetchall()  # list of tuples

def format_table(headers, rows):
    """Return a simple text table without external libraries."""
    # Compute column widths
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))

    # Row builders
    def fmt_row(row_vals):
        return " | ".join(str(v).ljust(widths[i]) for i, v in enumerate(row_vals))

    sep = "-+-".join("-" * w for w in widths)

    lines = [fmt_row(headers), sep]
    for r in rows:
        lines.append(fmt_row(r))
    return "\n".join(lines)

if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)
    try:
        ensure_table(conn)
        seed_if_empty(conn)

        # Basic CRUD example (update + delete are commented for safety)
        # conn.execute("UPDATE students SET grade = ? WHERE name = ?", (95, "John"))
        # conn.execute("DELETE FROM students WHERE name = ?", ("Alice",))
        # conn.commit()

        students = fetch_students(conn)
        print(format_table(["ID", "Name", "Grade"], students))
    finally:
        conn.close()
