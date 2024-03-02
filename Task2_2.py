import sqlite3
def write_students():
    with open('students.csv', 'r') as f:
        line = f.readline()
        results = []
        while line:
            line = line[:-1]
            results.append(line.split(','))
            line = f.readline()

    results = results[1:]

    for result in results:
        #print(result)
        query = """ INSERT INTO Student(MatricNo, Name, Class, IndexNo, Gender)
                VALUES (?,?,?,?,?)
                """
        conn = sqlite3.connect('seating.db')
        conn.execute(query, (result[0], result[1], result[2], result[3], result[4]))
        conn.commit()
        conn.close()
        #print("inserted")
                     

#write_students()


def write_class():
    with open('classgroups.csv', 'r') as f:
        line = f.readline()
        results = []
        while line:
            line = line[:-1]
            results.append(line.split(','))
            line = f.readline()

    results = results[1:]

    for result in results:
        #print(result)
        query = """ INSERT INTO ClassGroup(ClassGroupID, ClassGroupName, Venue)
                VALUES (?,?,?)
                """
        conn = sqlite3.connect('seating.db')
        conn.execute(query, (result[0], result[1], result[2]))
        conn.commit()
        conn.close()
        #print("inserted")

#write_class()

def SCR():
    with open('scr.csv', 'r') as f:
        line = f.readline()
        results = []
        while line:
            line = line[:-1]
            results.append(line.split(','))
            line = f.readline()

    results = results[1:]

    for result in results:
        #print(result)
        query = """ INSERT INTO SCR(MatricNo, ClassGroupID)
                VALUES (?,?)
                """
        conn = sqlite3.connect('seating.db')
        conn.execute(query, (result[0], result[1]))
        conn.commit()
        conn.close()
        #print("inserted")

#SCR()

    
