SELECT Student.Class, Student.IndexNo, Student.name, ClassGroup.ClassGroupName
FROM Student, ClassGroup, SCR
WHERE ClassGroup.ClassGroupName = "Comp_4AB"
AND ClassGroup.ClassGroupID = SCR.ClassGroupID
AND Student.MatricNo = SCR.MatricNo
ORDER BY Student.Class ASC