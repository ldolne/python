-- Théorie - Test des fonctions
SELECT CAST(birth_date AS char(10)) AS "Date de naissance"
FROM student;

SELECT TO_CHAR(birth_date, 'DD-MM-YYYY') AS "Date de naissance"
FROM student;

SELECT TO_CHAR(CURRENT_TIMESTAMP, 'YYYY-MM-DD HH24:MI:SS') AS "Date du jour",
TO_CHAR(NOW(), 'YYYY-MM-DD HH24:MI:SS') AS "Date du jour formatée",
CURRENT_DATE AS "Date uniquement", CURRENT_TIME AS "Heure uniquement";

SELECT BIT_LENGTH('Kim Basinger') AS "Longueur de la chaine de caractères";

SELECT ABS(-1.0) AS "val1", ABS(0.0) AS "val2", ABS(1.1) AS "val3";
SELECT @ -1.0 AS "val1", @ 0.0 AS "val2", @ 1.1 AS "val3";

SELECT 38.0 / 5 AS "Division", 38/5 AS "Division Entière", 38 % 5 AS "Reste";
SELECT 38.0 / 5 AS "Division", 38/5 AS "Division Entière", MOD (38, 5) AS "Reste";

SELECT SUBSTRING('Basinger' FROM 4 FOR 3)
AS "Caractères 4, 5 et 6";
SELECT last_name, SUBSTRING(first_name FROM 1 FOR 1)
AS "Initiale du prénom"
FROM student;

SELECT LEFT('Basinger', 4) AS "4 premiers caractères";
SELECT last_name, RIGHT(first_name, 1)
AS "Dernière lettre du prénom"
FROM student;

SELECT REPLACE(' Kim Basinger ', ' ' , '') AS "Sans espace",
REPLACE('1111000010101010', '1', '0') AS "Sans 1";

SELECT LTRIM(' Kim Basinger ') AS "LTRIM",
RTRIM(' Kim Basinger ') AS "RTRIM",
TRIM(' Kim Basinger ') AS "TRIM";

SELECT COUNT(*) AS "Total des lignes",
COUNT(first_name) AS "Total des prénoms",
COUNT(DISTINCT first_name) AS "Total des prénoms sans doublons"
FROM student;

SELECT MAX(year_result) AS "Résultat le plus élevé",
MIN(year_result*5) AS "Pourcentage le plus faible",
MAX(CHAR_LENGTH(last_name)) AS "Taille du nom le plus long"
FROM student;

SELECT SUM(year_result) AS "Somme des résultats annuels",
SUM(year_result)::FLOAT/COUNT(*) AS "Moyenne générale"
FROM student;

SELECT AVG(year_result) AS "Moyenne générale",
AVG(DATE_PART('YEAR',CURRENT_DATE)-DATE_PART('YEAR', birth_date))
AS "Moyenne d'âge"
FROM student;


SELECT last_name, first_name, year_result,
CASE
  WHEN year_result BETWEEN 18 AND 20 THEN 'Excellent'
  WHEN year_result BETWEEN 16 AND 17 THEN 'Très bien'
  WHEN year_result BETWEEN 14 AND 15 THEN 'Bien'
  WHEN year_result BETWEEN 12 AND 13 THEN 'Suffisant'
  WHEN year_result BETWEEN 10 AND 11 THEN 'Faible'
  WHEN year_result BETWEEN 8 AND 9 THEN 'Insuffisant'
  ELSE 'Insuffisance grave'
END AS "Note globale"
FROM student;

SELECT last_name, first_name,
CASE section_id
  WHEN '1010' THEN 'BSc Management'
  WHEN '1320' THEN 'MA Sociology'
  ELSE NULL
END AS "Nom de section"
FROM student;

SELECT last_name, first_name, year_result, NULLIF(year_result, 7) AS
"Résultats sauf les 7/20"
FROM student
ORDER BY first_name;

-- Exercices module 3 Les Fonctions
-- Exo 2.3.1
-- Parce que c'est une fonction d'agrégation et que celles-ci, sauf exceptions, ne prennent pas en compte les valeurs NULL.

-- Exo 2.3.2
-- On compte le nombre de lignes, non les valeurs de celles-ci.

-- Exo 2.3.3
-- Faux

-- Exo 2.3.4
-- Faux

-- Exo 2.3.5
-- VRAI

-- Exo 2.3.6
SELECT COUNT(*) -- il manque les parenthèses 
FROM student;
SELECT COUNT(student_id) as student_id_count, COUNT(login) as login_count -- login doit aussi être traité par une fonction agrégée, ou apapraitre dans un group_by
FROM student;
SELECT MIN(year_result), MAX(birth_date) -- correct
FROM student
WHERE year_result > 12;

-- Exo 2.3.7
SELECT AVG(year_result)
FROM student;

-- Exo 2.3.8
SELECT MAX(year_result)
FROM student;

-- Exo 2.3.9
SELECT SUM(year_result)
FROM student;

-- Exo 2.3.10
SELECT MIN(year_result)
FROM student;

-- Exo 2.3.11
SELECT COUNT(*)
FROM student;

-- Exo 2.3.12
SELECT login, DATE_PART('YEAR', birth_date)
FROM student
WHERE DATE_PART('YEAR', birth_date) > ('1970');

-- Exo 2.3.13
SELECT login, last_name
FROM student
WHERE CHAR_LENGTH(last_name) >= 8;

-- Exo 2.3.14
SELECT UPPER(last_name) as "Nom de Famille", first_name
FROM student
WHERE year_result >= 16
ORDER BY year_result;

-- Exo 2.3.22
-- TMmonth => TM (Template Mode) var rechercher la variable de langue initialisée sur le serveur
SET lc_time = 'fr-FR.UTF-8'; -- pour définir la variable
SELECT TO_CHAR(NOW(), 'TMMon DD YYYY HH:MI:SS AM');