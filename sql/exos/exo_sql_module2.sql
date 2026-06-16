-- Exo 2.1.1
SELECT last_name, first_name as "F name" -- manque les deux " " autour de l'alias
FROM student;

SELECT last_name lname, first_name as fname -- oui, car AS est optionnel et "fname" écrit en un mot ne requiert pas de guillemets
FROM student;

SELECT last_name || '_' || first_name as name -- manque ' ' guillemets simples autour de _
FROM student;

SELECT last_name || first_name as name, -- mauvais opérateur de concaténation : + au lieu de || 
Year_result * 10 result -- x au lieu de * ; virgule en trop ; les colonnes sont bien case insensitive, donc c'est ok
FROM student;

-- Exo 2.1.2
SELECT last_name, birth_date, login, year_result
FROM student;

-- Exo 2.1.3
SELECT first_name || ' ' || last_name as "Nom complet", student_id, birth_date
FROM student;

-- Exo 2.1.4
SELECT student_id || ' | ' || first_name || ' | ' || last_name || ' | ' || birth_date || ' | ' || login || ' | ' || section_id || ' | ' || year_result as "Info Etudiant"
FROM student;
SELECT student as "Info complètes"
FROM student;


-- Exo 2.2.1
SELECT login, year_result
FROM student
WHERE year_result > 16;

-- Exo 2.2.2
SELECT last_name, section_id
FROM student
WHERE first_name = 'Georges'; -- attention : "" pour définir des colonnes, '' pour définir des strings
-- IN('Georges', 'georges')
-- LIKE 'Georges'
-- ILIKE 'georges'
-- lower(first_name) = 'georges'

-- Exo 2.2.3
SELECT last_name, year_result
FROM student
WHERE year_result BETWEEN 12 and 16;
-- WHERE year_result >= 12 AND year_result <= 16;
-- WHERE year_result in (12,13,14,15,16); -- overkill

-- Exo 2.2.4
SELECT last_name, section_id, year_result
FROM student
WHERE section_id NOT IN(1010, 1020, 1110);
-- WHERE section_id != 1010 AND section_id != 1020 AND section_id != 1110;

-- Exo 2.2.5
SELECT last_name, section_id
FROM student
WHERE last_name like '%r';

-- Exo 2.2.6
SELECT last_name, year_result
FROM student
WHERE last_name like '__n%' and year_result > 10;

-- Exo 2.2.7
SELECT last_name, year_result
FROM student
WHERE year_result <= 3
ORDER BY year_result DESC;

-- Exo 2.2.8
SELECT last_name || ' ' || first_name as name, year_result
FROM student
WHERE section_id = 1010
ORDER BY name ASC;

-- Exo 2.2.9
SELECT last_name, section_id, year_result
FROM student
WHERE section_id IN (1010, 1020) and year_result NOT BETWEEN 12 and 18
ORDER BY section_id ASC;

-- Exo 2.2.10
SELECT last_name, section_id, year_result, (year_result/20.0)*100 AS result_percentage -- result_percentage peut être utilisé dans un ORDER BY mais pas un WHERE par ex., car le code SQL exécute le SELECT après le WHERE ; -- OU year_result * 5 AS result_percentage
FROM student
-- WHERE section_id like '13%' AND (year_result/20.0)*100 <= 60 -- 20.0 assure que la division se fera en float et non en integer, ce qui équivaudrait à 0
WHERE section_id BETWEEN 1300 AND 1399 AND (year_result/20.0)*100 <= 60
-- ORDER BY year_result DESC;
ORDER BY result_percentage DESC;