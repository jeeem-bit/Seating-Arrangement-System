import sqlite3

query = """SELECT Student.Class, Student.IndexNo, Student.Name
                   FROM Student, SCR, ClassGroup
                   WHERE ClassGroup.ClassGroupName = "Comp_4AB"
                   AND ClassGroup.ClassGroupID = SCR.ClassGroupID
                   AND SCR.MatricNo = Student.MatricNo"""


conn = sqlite3.connect("seating.db")
cursor = conn.execute(query)
results = cursor.fetchall()
rows=[]
count = 0
while len(results)>0:
    temp = []
    while count != 5:
        if len(results)<=0:
            break
        stu_class=results[0][0]
        index=results[0][1]
        name=results[0][2]
        temp.append("(" + stu_class + "(" + str(index) + ")" +"," +name + ")")
        results = results[1:]
        count += 1
    rows.append(temp)
    count = 0
        
    
cursor.close()
conn.close()
print(rows)
