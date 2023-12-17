import mysql.connector
import config

host = "localhost"
user = "root"
database = "studentdb"

try:
    # Connect to the MySQL server
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=config.password,
        database=database
    )

    if connection.is_connected():
        print("Connected to MySQL database")

        # Perform database operations start here
        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()
        
        # Create table
        # cursor.execute("CREATE TABLE students (ID INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, age INT)")
        
        # queries = "INSERT INTO students (name, age) VALUES(%s, %s)"
        # students = [("Anthony", 30), ("Pseth", 30), ("Nick", 26), ("Joel", 29)]

        # # # Example: Execute a SELECT query
        # cursor.executemany(queries, students)
        
        # connection.commit()
        
        cursor.execute("SELECT * FROM students")

        # # Fetch all rows
        rows = cursor.fetchall()

        # # Display the results
        for row in rows:
            print(row)

        # Close the cursor
        cursor.close()

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    # Close the database connection in the finally block
    if connection.is_connected():
        connection.close()
        print("Connection closed")




