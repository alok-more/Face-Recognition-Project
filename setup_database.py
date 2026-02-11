import sqlite3

def setup_database():
    """
    Initialize SQLite database with student table for face recognition system
    """
    try:
        # Connect to database (creates if doesn't exist)
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        
        # Create student table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS student (
                ID INTEGER PRIMARY KEY,
                Name TEXT NOT NULL,
                Age INTEGER NOT NULL
            )
        ''')
        
        conn.commit()
        print("✅ Database setup successful!")
        print("📊 Table 'student' created with columns: ID, Name, Age")
        
        # Display existing records
        cursor.execute("SELECT COUNT(*) FROM student")
        count = cursor.fetchone()[0]
        print(f"📝 Current records in database: {count}")
        
        conn.close()
        
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🗄️ Setting up Face Recognition Database...")
    print("-" * 50)
    setup_database()