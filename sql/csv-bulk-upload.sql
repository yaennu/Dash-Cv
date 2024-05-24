DROP TABLE Cv.Cv;

CREATE TABLE Cv.Cv (
    Thema NVARCHAR(50) NOT NULL,
    ThemaValue TINYINT NOT NULL,
    Start DATE NOT NULL,
    Ende DATE NOT NULL,
    Wert INT,
    BezeichnungKurz NVARCHAR(50),
    Bezeichnung NVARCHAR(100),
    Ort NVARCHAR(100)
);

CREATE TABLE Cv.Hobbies (
    Hobby NVARCHAR(50) NOT NULL,
    Prozent TINYINT NOT NULL
);

CREATE TABLE Cv.Interests (
    Thema NVARCHAR(50) NOT NULL,
    Bezeichnung NVARCHAR(50) NOT NULL,
    Wert TINYINT NOT NULL
);

/* BULK INSERT does not work
BULK INSERT Cv.Cv
FROM 'C:\\DefaultWD\\cv.csv'
WITH
(
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);*/


ALTER TABLE Cv.Cv
DROP COLUMN BezeichnungKurz;

ALTER TABLE Cv.Cv
ADD BezeichnungKurz NVARCHAR(50);
