import sqlite3

random_data = [
["John", "Smith", "Doe", "123 Main St, Cityville", "1234567890", "john@example.com", "1995-05-20", "Male"],
["Alice", "Johnson", "Mary", "456 Elm St, Townsville", "9876543210", "alice@example.com", "1990-10-15", "Female"],
["Michael", "Brown", "Richard", "789 Oak St, Villageton", "5551234567", "michael@example.com", "1988-03-08", "Male"],
["Emily", "Davis", "Elizabeth", "321 Pine St, Hamletown", "7779876543", "emily@example.com", "1992-12-01", "Female"],
["David", "Wilson", "Robert", "555 Cedar St, Forestville", "9993334445", "david@example.com", "1985-07-30", "Male"],
["Sarah", "Jones", "Ann", "234 Maple Ave, Riverside", "5557778888", "sarah@example.com", "1993-09-12", "Female"],
["Daniel", "Martinez", "James", "876 Oakwood Blvd, Hilltown", "3332221111", "daniel@example.com", "1997-02-28", "Male"],
["Jessica", "Thompson", "Marie", "987 Willow Ln, Lakeside", "4445556666", "jessica@example.com", "1991-06-25", "Female"],
["Ryan", "Garcia", "Lee", "654 Birch Rd, Mountainview", "8889990000", "ryan@example.com", "1987-11-18", "Male"],
["Lauren", "Rodriguez", "Michelle", "432 Pinecrest Dr, Valley City", "2224445555", "lauren@example.com", "1989-04-05", "Female"]
]

conn = sqlite3.connect("student.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, name text, fname text, mname text, \
                address text, mobno integer,email text, dob integer, gender text)")

cur.executemany("INSERT INTO student VALUES (NULL,?,?,?,?,?,?,?,?)",random_data)

print(conn.commit())
conn.close()
