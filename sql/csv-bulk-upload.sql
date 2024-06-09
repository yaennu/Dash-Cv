DROP TABLE Cv.Skills;

CREATE TABLE Cv.Test (
    Theme NVARCHAR(50) NOT NULL,
    Order TINYINT NOT NULL,
    'Start' DATE NOT NULL,
    'End' DATE NOT NULL,
    'Value' INT,
    DescriptionShort NVARCHAR(50),
    'Description' NVARCHAR(100),
    Place NVARCHAR(100)
);

--CREATE SCHEMA Cv;

/* BULK INSERT does not work
BULK INSERT Cv.Cv
FROM 'C:\\DefaultWD\\cv.csv'
WITH
(
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);*/

BULK INSERT Cv.Test
FROM 'C:\\DefaultWD\\Dash-Cv\\Cv.csv'
WITH ( FORMAT = 'CSV');


ALTER TABLE Cv.Cv
DROP COLUMN BezeichnungKurz;

ALTER TABLE Cv.Cv
ADD BezeichnungKurz NVARCHAR(50);
