import sqlite3

#The connect operation makes a "connection" to the database stored in the file music.sqlite3 in the current directory. If the file does not exist, it will be created. The reason this is called a "connection" is that sometimes the database is stored on a separate "database server" from the server on which we are running our application.
conn = sqlite3.connect('music.sqlite')
# A cursor is like a file handle that we can use to perform operations on the data stored in the database. Calling cursor() is very similar conceptually to calling open() when dealing with text files.
cur = conn.cursor()

#The first SQL command removes the Tracks table from the database if it exists. This pattern is simply to allow us to run the same program to create the Tracks table over and over again without causing an error. Note that the DROP TABLE command deletes the table and all of its contents from the database (i.e., there is no "undo").
cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks(title TEXT, plays INTEGER)')

#The SQL INSERT command indicates which table we are using and then defines a new row by listing the fields we want to include (title, plays) followed by the VALUES we want placed in the new row. We specify the values as question marks (?, ?) to indicate that the actual values are passed in as a tuple ( 'My Way', 15 ) as the second parameter to the execute() call.
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
    ('Thunderstruck', 20))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
    ('My Way', 15))
conn.commit()

print('Tracks:')
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
     print(row)

cur.execute('DELETE FROM Tracks WHERE plays < 100')

cur.close()
