-- Exo 2.1.1
SELECT last_name, first_name as "F name" -- manque les deux " " autour de l'alias
FROM student;

SELECT last_name lname, first_name as fname -- oui, car AS est optionnel et "fname" écrit en un mot ne requiert pas de guillemets
FROM student;

SELECT last_name || '_' || first_name as name -- manque ' ' guillemets simples autour de _
FROM student;

SELECT last_name || first_name as name, -- mauvais opérateur de concaténation : + au lieu de || 
Year_result * 10 result -- x au lieu de * ; les colonnes sont bien case insensitive, donc c'est ok
FROM student;

-- Exo 2.1.2
SELECT last_name, birth_date, login, year_result
FROM student;

-- Exo 2.1.3
SELECT first_name || ' ' || last_name as "Nom complet", student_id, birth_date
FROM student;

-- Exo 2.1.4
SELECT student_id || '|' || first_name || '|' || last_name || '|' || birth_date || '|' || login || '|' || section_id || '|' || year_result as "Info Etudiant"
FROM student;


-- Exo 2.2.1
SELECT login, year_result
FROM student
WHERE year_result > 16;

-- Exo 2.2.2
SELECT last_name, section_id
FROM student
WHERE first_name = 'Georges'; -- attention : "" pour définir des colonnes, '' pour définir des strings

-- Exo 2.2.3
SELECT last_name, year_result
FROM student
WHERE year_result BETWEEN 12 and 16;

-- Exo 2.2.4
SELECT last_name, section_id, year_result
FROM student
WHERE section_id NOT IN('1010', '1020', '1110');

-- Exo 2.2.5
SELECT last_name, section_id
FROM student
WHERE last_name like '%r';

-- Exo 2.2.6

-- Exo 2.2.7

-- Exo 2.2.8

-- Exo 2.2.9

-- Exo 2.2.10

-- Exo 2.2.11