import sqlite3
from datetime import datetime, time


def in_between(now, start, end):
    if start <= end:
        return start <= now < end
    else:  # over midnight e.g., 23:30-04:15
        return start <= now or now < end


print("night" if in_between(datetime.now().time(), time(23), time(4)) else "day")

# conn = sqlite3.connect("test_database.db")
# cur = conn.cursor()
# cur.execute("CREATE TABLE if not exists People \
#     (FirstName TEXT, \
#      LastName TEXT, \
#      Age INT \
# )")


# peopleValues = (('Luigi', 'Vercotti', 43), ('Arthur',
#                                             'Belling', 28), ('Ron', 'Obvious', 42))

# with sqlite3.connect("test_database.db") as conn:
#     cur = conn.cursor()
#     cur.execute("DROP TABLE IF EXISTS People")
#     cur.execute("CREATE TABLE People (FirstName TEXT, LastName TEXT, Age INT)")
#     cur.executemany("INSERT INTO People VALUES (?,?,?)", peopleValues)

#     cur.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
#     while True:
#         row = cur.fetchone()
#         if row is None:
#             break
#         print(row)
