# SQL => Structured Query Language

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
    
    db.execute(
        """
        INSERT INTO students (name, age, grade) VALUES
        ('Lucas', 23, 10),
        ('Carlos', 8, 2);
        """
    )
    
    db.execute("""DELETE FROM students""") # Delete all data of that table
    #! Normally it would be used the `TRUNCATE` cmd, but it doesn't exists in
    #! Python's SQLite3 lib.
    
    conn.commit()


    db.close()
    conn.close()

if __name__ == '__main__':
    main()
    
#! OBS: This way of usign Python and SQL isn't advised, because makes your code
#! vunerable to an SQL Injection atack.