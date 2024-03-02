from flask import Flask, render_template, request
import sqlite3

app=Flask(__name__)

@app.route('/', methods=["GET","POST"])
def form():
    if request.method == "GET":
        return render_template("form.html")
    else:
        classgroupname = request.form["classgroupname"]

        query = """SELECT Student.Class, Student.IndexNo, Student.Name
                   FROM Student, SCR, ClassGroup
                   WHERE ClassGroup.ClassGroupName = ?
                   AND ClassGroup.ClassGroupID = SCR.ClassGroupID
                   AND SCR.MatricNo = Student.MatricNo"""


        conn = sqlite3.connect("seating.db")
        cursor = conn.execute(query, classgroupname)
        results = cursor.fetchall()
        cursor.close()
        conn.close()

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
        
        return render_template("display.html", classgroupname=classgroupname, rows=rows)

if __name__ == "__main__":
    app.run()






