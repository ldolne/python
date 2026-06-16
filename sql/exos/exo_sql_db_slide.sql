-- Exo 1.5
CREATE TABLE Section (
  section_id int NOT NULL,
  section_name varchar(50),
  delegate_id int NOT NULL,
  CONSTRAINT PK_section PRIMARY KEY(section_id)
);

CREATE TABLE Professor (
  professor_id int NOT NULL,
  professor_name varchar(30) NOT NULL,
  professor_surname varchar(30) NOT NULL,
  section_id int NOT NULL,
  professor_office int NOT NULL,
  professor_email varchar(30) NOT NULL,
  professor_hire_date timestamp NOT NULL,
  professor_wage int NOT NULL,
  CONSTRAINT PK_professor PRIMARY KEY (professor_id),
  constraint FK_professor_section foreign key (section_id) references section (section_id)
);

CREATE TABLE Course (
  course_id varchar(8) NOT NULL ,
  course_name varchar(200) NOT NULL ,
  course_ects decimal(3,1) NOT NULL,
  professor_id int NOT NULL,
  CONSTRAINT PK_course PRIMARY KEY (course_id),
  constraint FK_course_professor foreign key (professor_id) references professor (professor_id)
);

CREATE TABLE Student (
  student_id int NOT NULL,
  first_name varchar(50),
  last_name varchar(50),
  birth_date timestamp,
  login varchar(50),
  section_id int,
  year_result int,
  course_id varchar(8) NOT NULL,
  CONSTRAINT PK_student PRIMARY KEY (student_id),
  constraint FK_student_section foreign key (section_id) references section (section_id),
  constraint FK_student_course foreign key (course_id) references course (course_id)
);

CREATE TABLE Grade (
  grade char(2) NOT NULL check (grade in ('E','TB','B','S','F','I','IG')),
  lower_bound int NOT NULL,
  upper_bound int NOT NULL,
  CONSTRAINT PK_grade PRIMARY KEY (grade)
);


-- INSERT DATA
delete from grade;
delete from student;
delete from course;
delete from professor;
delete from section;

INSERT INTO section VALUES (1010, 'BSc Management', 12);
INSERT INTO section VALUES (1020, 'MSc Management', 9);
INSERT INTO section VALUES (1111, 'BSc Economics', 15);
INSERT INTO section VALUES (1120, 'MSc Economics', 6);
INSERT INTO section VALUES (1310, 'BA Sociology', 23);
INSERT INTO section VALUES (1320, 'MA Sociology', 6);

INSERT INTO professor VALUES (1,'zidda', 'pietro', 1020, 402, 'pzidda', '2004-12-11', 1900);
INSERT INTO professor VALUES (2,'decrop', 'alain', 1120, 403, 'adecrop', '2003-05-09', 1950);
INSERT INTO professor VALUES (3,'giot', 'pierre', 1310, 404, 'pgiot', '2002-12-21', 2100);
INSERT INTO professor VALUES (4,'lecourt', 'christelle', 1310, 406, 'clecourt', '2003-05-07', 1750);
INSERT INTO professor VALUES (5,'scheppens', 'georges', 1020, 410, 'gscheppens', '1986-10-09', 2450);
INSERT INTO professor VALUES (6,'louveaux', 'francois', 1111, 407, 'flouveaux', '1990-05-07', 2200);

INSERT INTO course VALUES ('EING2234', 'Derivatives', 3.0, 3);
INSERT INTO course VALUES ('ECGE2184', 'Marketing management', 3.5, 2);
INSERT INTO course VALUES ('EING2283', 'Marketing engineering', 4.0, 1);
INSERT INTO course VALUES ('ECGE2183', 'Financial Management', 4.0, 3);
INSERT INTO course VALUES ('EING2383', 'Supply chain management et e-business', 2.5, 5);

INSERT INTO student VALUES (1, 'Georges', 'Lucas', '1944-05-17 00:00:00', 'glucas', 1320, 10, 'EING2234');
INSERT INTO student VALUES (2, 'Clint', 'Eastwood', '1930-05-31 00:00:00', 'ceastwoo', 1010, 4, 'EING2234');
INSERT INTO student VALUES (3, 'Sean', 'Connery', '1930-08-25 00:00:00', 'sconnery', 1020, 12, 'ECGE2184');
INSERT INTO student VALUES (4, 'Robert', 'De Niro', '1943-08-17 00:00:00', 'rde niro', 1111, 3, 'EING2234');
INSERT INTO student VALUES (5, 'Kevin', 'Bacon', '1958-07-08 00:00:00', 'kbacon', 1120, 16, 'EING2283');
INSERT INTO student VALUES (6, 'Kim', 'Basinger', '1953-12-08 00:00:00', 'kbasinge', 1310, 19, 'EING2283');
INSERT INTO student VALUES (7, 'Johnny', 'Depp', '1963-06-09 00:00:00', 'jdepp', 1111, 11, 'EING2234');
INSERT INTO student VALUES (8, 'Julia', 'Roberts', '1967-10-28 00:00:00', 'jroberts', 1120, 17, 'EING2283');
INSERT INTO student VALUES (9, 'Natalie', 'Portman', '1981-06-09 00:00:00', 'nportman', 1010, 4, 'EING2234');
INSERT INTO student VALUES (10, 'Georges', 'Clooney', '1961-05-06 00:00:00', 'gclooney', 1020, 4, 'ECGE2184');
INSERT INTO student VALUES (11, 'Andy', 'Garcia', '1956-04-12 00:00:00', 'agarcia', 1111, 19, 'EING2283');
INSERT INTO student VALUES (12, 'Bruce', 'Willis', '1955-03-19 00:00:00', 'bwillis', 1010, 6, 'EING2234');
INSERT INTO student VALUES (13, 'Tom', 'Cruise', '1962-07-03 00:00:00', 'tcruise', 1020, 4, 'ECGE2184');
INSERT INTO student VALUES (14, 'Reese', 'Witherspoon', '1976-03-22 00:00:00', 'rwithers', 1020, 7, 'ECGE2183');
INSERT INTO student VALUES (15, 'Sophie', 'Marceau', '1966-11-17 00:00:00', 'smarceau', 1111, 6, 'EING2283');
INSERT INTO student VALUES (16, 'Sarah', 'Michelle Gellar', '1977-04-14 00:00:00', 'smichell', 1020, 7, 'ECGE2184');
INSERT INTO student VALUES (17, 'Alyssa', 'Milano', '1972-12-19 00:00:00', 'amilano', 1111, 7, 'EING2283');
INSERT INTO student VALUES (18, 'Jennifer', 'Garner', '1972-04-17 00:00:00', 'jgarner', 1120, 18, 'EING2283');
INSERT INTO student VALUES (19, 'Michael J.', 'Fox', '1969-06-20 00:00:00', 'mfox', 1310, 3, 'EING2283');
INSERT INTO student VALUES (20, 'Tom', 'Hanks', '1956-07-09 00:00:00', 'thanks', 1020, 8, 'ECGE2184');
INSERT INTO student VALUES (21, 'David', 'Morse', '1953-10-11 00:00:00', 'dmorse', 1111, 2, 'EING2283');
INSERT INTO student VALUES (22, 'Sandra', 'Bullock', '1964-07-26 00:00:00', 'sbullock', 1010, 2, 'ECGE2183');
INSERT INTO student VALUES (23, 'Keanu', 'Reeves', '1964-09-02 00:00:00', 'kreeves', 1020, 10, 'EING2234');
INSERT INTO student VALUES (24, 'Shannen', 'Doherty', '1971-04-12 00:00:00', 'sdoherty', 1320, 2, 'ECGE2183');
INSERT INTO student VALUES (25, 'Halle', 'Berry', '1966-08-14 00:00:00', 'hberry', 1320, 18, 'ECGE2183');

INSERT INTO grade VALUES ('IG', 0, 7);
INSERT INTO grade VALUES ('I', 8, 9);
INSERT INTO grade VALUES ('F', 10, 11);
INSERT INTO grade VALUES ('S', 12, 13);
INSERT INTO grade VALUES ('B', 14, 15);
INSERT INTO grade VALUES ('TB', 16, 17);
INSERT INTO grade VALUES ('E', 18, 20);

-- Exo 1.6
ALTER TABLE section ALTER COLUMN delegate_id TYPE int;

ALTER TABLE section ADD CONSTRAINT fk_student_section_delegate
FOREIGN KEY(delegate_id)
REFERENCES student(student_id) ON DELETE SET NULL;

ALTER TABLE student DROP CONSTRAINT FK_student_course;
ALTER TABLE student DROP COLUMN course_id;

ALTER TABLE student ALTER COLUMN student_id ADD GENERATED ALWAYS AS IDENTITY;

ALTER TABLE student DROP CONSTRAINT FK_student_section;
ALTER TABLE professor DROP CONSTRAINT FK_professor_section;
ALTER TABLE section ALTER COLUMN section_id TYPE char(4);
ALTER TABLE student ALTER COLUMN section_id TYPE char(4);
ALTER TABLE professor ALTER COLUMN section_id TYPE char(4);
ALTER TABLE student ADD CONSTRAINT FK_student_section FOREIGN KEY(section_id) REFERENCES section(section_id);
ALTER TABLE professor ADD CONSTRAINT FK_professor_section FOREIGN KEY(section_id) REFERENCES section(section_id);

-- Exo 1.7
-- PAS FAIT !


SELECT CONCAT(first_name, ' ', last_name) AS "Nom complet",
login || student_id AS "Code étudiant"
FROM student;

SELECT DISTINCT first_name FROM student;
SELECT first_name FROM student;

SELECT distinct(section_id, first_name), section_id, first_name, last_name
FROM student
ORDER BY section_id, first_name, last_name;

SELECT distinct on(section_id, first_name) section_id, first_name, last_name
FROM student
ORDER BY section_id, first_name, last_name; -- colonnes pas affichées

SELECT student_id, first_name, last_name, year_result
FROM student
WHERE first_name ILIKE 'J%';


