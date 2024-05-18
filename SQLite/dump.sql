BEGIN TRANSACTION;
CREATE TABLE Employees(ID INTEGER PRIMARY KEY                     AUTOINCREMENT NOT NULL, FName TEXT NOT NULL,                     LName TEXT NOT NULL, Age INTEGER NOT NULL, Address TEXT,                     Salary REAL, HireDate TEXT, 'Image'                     BLOB DEFAULT NULL);
INSERT INTO "Employees" VALUES(1,'Chris','Poopedi',27,'Polokwane',3000.0,'2024-05-18',NULL);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('Employees',1);
COMMIT;
