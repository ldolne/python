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
select last_name, first_name, birth_date as "Date de Naissance", year_result
from student
where date_part('month',birth_date) = 
(select date_part('month',professor_hire_date) 
from professor 
where professor_name = 'giot')
order by year_result DESC;

-- Exo 2.7.5
select last_name, first_name, year_result
from student
where student_id in (
select student_id 
from student s, grade g 
where year_result between g.lower_bound and g.upper_bound 
and g.grade = 'TB');

-- Exo 2.7.6
-- Version avec un join
select last_name, first_name, section_id
from student
where section_id in
(select se.section_id
from section se, student st
where se.delegate_id = st.student_id and last_name = 'Marceau');

-- Version full subqueries
select last_name, first_name, section_id
from student
where section_id =
(select section_id
from section
where delegate_id = 
(select student_id from student where last_name = 'Marceau'));

-- Exo 2.7.7
select section_id, section_name
from section
where section_id in
(select section_id
from student
group by section_id
having count(student_id) > 4);

-- Exo 2.7.8
select last_name, first_name, section_id
from student
where year_result in
(select max(year_result)
from student
group by section_id)
and section_id not in
(select section_id
from student
group by section_id
having avg(year_result) < 10);

-- Exo 2.7.9
-- With limit
select section_id, avg(year_result) as avg
from student
group by section_id
order by section_id DESC
limit 1;

-- With all
select section_id, avg(year_result)
from student
group by section_id
having avg(year_result) 
>= ALL(
select avg(year_result)
from student
group by section_id);

-- With max
select section_id, avg(year_result)
from student
group by section_id
having avg(year_result) = (select max(ttable.average)
from (select avg(year_result) as average
from student
group by section_id) as ttable);

-- With with
with moyennes AS (
	select section_id, avg(year_result) as average
	from student
	group by section_id
)
select section_id, average
from moyennes
where average = (select max(average) from moyennes);