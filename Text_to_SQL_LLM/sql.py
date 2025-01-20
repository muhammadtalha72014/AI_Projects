import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('Talha','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Abdullah','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Haroon','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Umer','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Hannia','DEVOPS','A',35)''')

## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()