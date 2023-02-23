select * from Students;

describe students;

alter table students
modify StudentID int primary key;

CREATE TABLE Courses (
    CourseID int,
    CName varchar(255),
    Duration int CHECK (Duration<100),
    Fees int,
    Batch_Size int CHECK (Batch_Size<10)
);


INSERT INTO Courses 
values('CDR234', 'DataStructures', 20, 10000, 5),
('CDR300', 'Python', 50, 20000, 10),
('CDR320', 'Java', 50, 20000, 10),
('CDR345', 'C++', 50, 20000, 10),
('CDR390', 'DevOPs', 40, 15000, 5),
('CDR380', 'AWS', 30, 20000, 8);

ALTER TABLE Courses
MODIFY CourseID varchar(255) PRIMARY KEY;

ALTER TABLE Courses
modify Batch_Size int CHECK (Batch_Size<=10);

ALTER TABLE Courses DROP CONSTRAINT courses_chk_3;

ALTER TABLE Courses
ADD CONSTRAINT  courses_chk_2 CHECK (Batch_Size<=10);


select * from Courses;

DESCRIBE Courses;

CREATE TABLE Enrollments(
	Order_Id int PRIMARY KEY auto_increment,
    Student_Id int NOT NULL,
    Course_Id varchar(255) NOT NULL,
    Is_Active bool default true,
    UNIQUE (Student_Id, Course_Id),
    FOREIGN KEY (Student_Id) REFERENCES students(StudentID),
    FOREIGN KEY (Course_Id) REFERENCES courses(CourseID)
);

INSERT INTO Enrollments (Student_Id, Course_Id)
values(2324, "CDR234");

DESCRIBE Enrollments;


select * from Enrollments;

INSERT INTO Enrollments (Student_Id, Course_Id)
values(43535, "CDR234");

select * from students;

INSERT INTO Enrollments (Student_Id, Course_Id)
values(654356, "CDR234");

INSERT INTO Enrollments (Student_Id, Course_Id)
values(654356, "CDR300");

select * from Enrollments;

select * from courses;


SELECT Students.StudentID, CONCAT(Students.FirstName, Students.LastName)  AS studentName,  Enrollments.Order_Id, Enrollments.Course_Id
FROM Students
INNER JOIN Enrollments ON Students.StudentID = Enrollments.Student_Id;

SELECT Students.StudentID, CONCAT(Students.FirstName, Students.LastName) AS studentName,  Enrollments.Order_Id, Enrollments.Course_Id
FROM Students
LEFT JOIN Enrollments ON Students.StudentID = Enrollments.Student_Id;


SELECT Students.StudentID, CONCAT(Students.FirstName, Students.LastName) AS studentName,  Enrollments.Order_Id, Enrollments.Course_Id
FROM Students
RIGHT JOIN Enrollments ON Students.StudentID = Enrollments.Student_Id;

SELECT Students.StudentID, CONCAT(Students.FirstName, Students.LastName) AS studentName,  Enrollments.Order_Id, Enrollments.Course_Id
FROM Students
CROSS JOIN Enrollments;

select Student_Id, count(Student_Id) as Enrolled_Courses
from Enrollments
group by Student_Id;

SELECT Students.StudentID,  count(Enrollments.Student_Id)
FROM Students
LEFT JOIN Enrollments ON Students.StudentID = Enrollments.Student_Id
group by Students.StudentID;

SELECT Students.StudentID,  count(Enrollments.Student_Id) as Enrolled_Courses
FROM Students
LEFT JOIN Enrollments ON Students.StudentID = Enrollments.Student_Id
group by Students.StudentID
having Enrolled_Courses>=1;

Update Enrollments
set Is_Active= false
where Student_Id=2324;

select * from enrollments;



show tables;

drop table enrollments;

drop table courses;
