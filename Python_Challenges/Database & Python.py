# CREATE A DATABASE TBL IN RAM NAMED ROSTER THAT
# INCLUDES THE FIELDS 'NAME', 'SPECIES', AND 'IQ'

import sqlite3

conn = sqlite3.connect("ram_database.db")
cur = conn.cursor()
cur.execute("CREATE TABLE if not exists Roster \
            (Name TEXT, \
            Species TEXT, \
            IQ INT \
            )")

populateValues = (('Jean-Baptiste Zorg', 'Human', 122),
                  ('Korben Dallas', 'Meat Popsicle', 100), ("Ak'not", "Mangalore", -5))

with sqlite3.connect("ram_database.db") as conn:
    c = conn.cursor()
    c.executemany("INSERT INTO Roster VALUES (?,?,?)", populateValues)
    c.execute("UPDATE Roster SET Species = 'Human' WHERE Species = 'Meat Popsicle'")

    c.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)

# Range practice
for i in range(4):
    print(i)

for i in range(3, -1, -1):
    print(i)

for i in range(8, 0, -2):
    print(i)
