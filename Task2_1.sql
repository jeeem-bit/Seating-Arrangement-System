CREATE TABLE "Student" (
	"MatricNo"	TEXT,
	"Name"	TEXT,
	"Class"	TEXT,
	"IndexNo"	INTEGER,
	"Gender"	TEXT,
	PRIMARY KEY("MatricNo")
);

CREATE TABLE "ClassGroup" (
	"ClassGroupID"	INTEGER UNIQUE,
	"ClassGroupName"	TEXT,
	"Venue"	TEXT,
	PRIMARY KEY("ClassGroupID" AUTOINCREMENT)
);

CREATE TABLE "SCR" (
	"MatricNo"	TEXT,
	"ClassGroupID"	INTEGER,
	PRIMARY KEY("MatricNo","ClassGroupID")
);

CREATE TABLE "SCR" (
	"MatricNo"	TEXT,
	"ClassGroupID"	INTEGER,
	FOREIGN KEY("MatricNo") REFERENCES "Student"("MatricNo"),
	FOREIGN KEY("ClassGroupID") REFERENCES "ClassGroup"("ClassGroupID"),
	PRIMARY KEY("MatricNo","ClassGroupID")
);