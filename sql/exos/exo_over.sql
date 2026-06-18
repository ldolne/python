/*Le OVER en PostgreSQL

Principe
OVER définit une fenêtre — un ensemble de lignes sur lequel une fonction est calculée 
— sans regrouper les lignes comme le ferait un GROUP BY.

OVER () — fenêtre sur toute la table
le salaire de chaque professeur et la moyenne globale des salaires à côté.
*/

SELECT
    professor_name,
    professor_surname,
    professor_wage,
    AVG(professor_wage) OVER () AS avg_global
FROM professor;
-- Toutes les lignes sont conservées. La moyenne globale apparaît à côté de chaque professeur.

/*PARTITION BY — calculer par groupe sans perdre les lignes
le salaire de chaque professeur et la moyenne des salaires de sa section.*/

SELECT
    professor_name,
    professor_surname,
    section_id,
    professor_wage,
    AVG(professor_wage) OVER (PARTITION BY section_id) AS avg_section
FROM professor;
-- Chaque professeur garde son détail, mais avg_section est calculée par section.

/* ORDER BY dans OVER — cumul
l'évolution de la masse salariale cumulée au fil des embauches.
*/
SELECT
    professor_name,
    professor_hire_date,
    professor_wage,
    SUM(professor_wage) OVER (ORDER BY professor_hire_date) AS cumul_salaires
FROM professor;

/*RANK / DENSE_RANK / ROW_NUMBER — classement
classer les professeurs par salaire décroissant.
*/
SELECT
    professor_name,
    professor_wage,
    RANK()        OVER (ORDER BY professor_wage DESC) AS rang_rank,
    DENSE_RANK()  OVER (ORDER BY professor_wage DESC) AS rang_dense,
    ROW_NUMBER()  OVER (ORDER BY professor_wage DESC) AS rang_row
FROM professor;

/* exemple
name    | salaire | row_number | rank | dense_rank
---------+---------+------------+------+------------
 Diana   |    9000 |          1 |    1 |          1
 Charlie |    7000 |          2 |    2 |          2
 Bob     |    7000 |          3 |    2 |          2
 Alice   |    7000 |          4 |    2 |          2
 Eve     |    5000 |          5 |    5 |          3
 Frank   |    4000 |          6 |    6 |          4
 */

/*Top 1 par section — le professeur le mieux payé de chaque section :*/

SELECT professor_name, section_id, professor_wage
FROM (
    SELECT
        professor_name,
        section_id,
        professor_wage,
        RANK() OVER (PARTITION BY section_id ORDER BY professor_wage DESC) AS rang
    FROM professor
) AS classement
WHERE rang = 1;

/*LAG / LEAD — ligne précédente / suivante
Tu veux voir l'évolution du salaire entre chaque embauche.*/

SELECT
    professor_name,
    professor_hire_date,
    professor_wage,
    LAG(professor_wage)  OVER (ORDER BY professor_hire_date) AS salaire_precedent,
    professor_wage - LAG(professor_wage) OVER (ORDER BY professor_hire_date) AS evolution
FROM professor;

/*GROUP BY vs OVER — la différence clé
*/
-- GROUP BY : une ligne par section, détail des profs perdu
SELECT section_id, AVG(professor_wage)
FROM professor
GROUP BY section_id;

-- OVER : tous les profs conservés, moyenne de leur section ajoutée
SELECT professor_name, section_id, professor_wage,
       AVG(professor_wage) OVER (PARTITION BY section_id)
FROM professor;

/*Résumé

OVER ()
Toute la table
Moyenne globale des salaires

OVER (PARTITION BY section_id)
Par section
Moyenne salariale par section

OVER (ORDER BY hire_date)
Cumul chronologique
Masse salariale cumulée

RANK()
Classement avec trous
Top prof par salaire

DENSE_RANK()
Classement sans trous
Idem sans sauter de rang

LAG()
Ligne précédente
Évolution salaire embauche par embauche*/