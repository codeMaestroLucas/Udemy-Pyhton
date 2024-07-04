def main() -> None:
    """Function used to run the main code."""
    from pathlib import Path
    import sqlite3
    
    ROOT_DIR = Path(__file__).parent
    DATABASE_FILE = ROOT_DIR / 'database.db'

    # Connect to the database
    conn = sqlite3.connect(DATABASE_FILE)
    db = conn.cursor() # Execute the commands in SQL.
    
    # db.executemany # To execute many commands
    db.execute(
        """
        CREATE TABLE students(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            grade REAL NOT NULL
        );
        """
    )
    
    values: list = [
        ('Lucas', 23, 10),
        ('Carlos', 8, 2)
        ]
    cmd = """ INSERT INTO students (name, age, grade) VALUES (?, ?, ?) ; """
    # for user in values:
    #     db.execute(cmd, user)
    db.executemany(cmd, values)
    
    
    # db.execute("""DELETE FROM students ;""") # Delete all data of that table
    
    conn.commit()


    db.close()
    conn.close()

if __name__ == '__main__':
    main()