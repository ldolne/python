-- Exo 2.7 - Requêtes imbriquées

-- Exo 2.7.1
select last_name, first_name, section_id
from student
where last_name != 'Roberts' and section_id =
(select section_id
from student
where last_name = 'Roberts')
order by last_name;

-- Exo 2.7.2
select last_name, first_name, year_result
from student
where year_result > 2 *
(select avg(year_result)
from student);

-- Exo 2.7.3
select section_id, section_name
from section
where section_id not in (select section_id from professor);

-- Exo 2.7.4
select date_part('month',birth_date)
from student;
select last_name, first_name, birth_date as "Date de Naissance", year_result
from student
where date_part('month',birth_date) = 
(select date_part('month',professor_hire_date) 
from professor 
where professor_name = 'giot')
order by year_result DESC;

-- Exo 2.7.5
