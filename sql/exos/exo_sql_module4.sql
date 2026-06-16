-- Exo GROUP BY... HAVING

-- Exo 2.4.1
-- Vrai, car on applique des opérations sur chacune des lignes, comme une boucle traitant chaque élément d'un ensemble.

-- Exo 2.4.2
-- Faux, le where est exécuté avant le group by

-- Exo 2.4.3
-- Faux, l'alias peut être utilisé dans le GROUP BY même s'il est exécuté après
-- La requête est lue en entier avant d'être exécutée, ce qui explique que l'alias est compris.

-- Exo 2.4.4
-- Faux, pas trié par le groupe by

-- Exo 2.4.5
-- Faux, c'est plutôt la colonne dans le SELECT qui, si elle n'est pas aggrégée, doit se trouver impérativement dans le GROUP BY

-- Exo 2.4.6
SELECT section_id, count(last_name) -- group by sur section_id et pas la colonne aggrégée
FROM student
group by section_id;

select section_id, avg(year_result)
from student 
-- where avg(year_result) > 50 -- fonctions agrégées pas autorisées dans where
group by section_id
having avg(year_result) > 50;

select section_id, avg(year_result) -- correct
from student
where year_result > 10
group by section_id;

-- Exo 2.4.7
select section_id, max(year_result) as "Résultat maximum"
from student
group by section_id
ORDER BY "Résultat maximum";

-- Exo 2.4.8
select section_id, avg(year_result)::NUMERIC(5,2) as "Moyenne"
from student
-- where section_id >= 1000 and section_id <= 1099
where cast(section_id as VARCHAR) like '10%'
group by section_id;

-- Exo 2.4.9
select EXTRACT(month from birth_date) as "Mois de naissance", avg(year_result)::NUMERIC(5,2) as "Moyenne"
from student
where date_part('year', birth_date) BETWEEN 1970 and 1985
group by EXTRACT(month from birth_date);

-- Exo 2.4.10
select section_id, avg(year_result) as "Moyenne"
from student
group by section_id
having count(*) > 3;

-- Exo 2.4.11
select section_id, avg(year_result) as "Moyenne", max(year_result) as "Résultat maximum"
from student
group by section_id
having avg(year_result) > 8;