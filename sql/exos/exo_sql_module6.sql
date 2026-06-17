-- Exos 6 - Jointures

-- Exo 2.6.1
select course_name, section_name, professor_name
from course c
inner join professor p on c.professor_id = p.professor_id
inner join section s on p.section_id = s.section_id;

-- Exo 2.6.2
select se.section_id, section_name, last_name
from section se
inner join student st on st.student_id = se.delegate_id
order by se.section_id DESC;

-- Exo 2.6.3
select se.section_id, section_name, professor_name
from section se
left join professor p on p.section_id = se.section_id;

-- Exo 2.6.4
select se.section_id, section_name, professor_name
from section se
inner join professor p on p.section_id = se.section_id;

-- Exo 2.6.5
select last_name, year_result, grade
from student st
join grade g
on st.year_result between g.lower_bound and g.upper_bound
where st.year_result >= 12
order by st.year_result DESC;

-- VIA WHERE
select last_name, year_result, grade
from student st, grade g
where st.year_result between g.lower_bound and g.upper_bound
and st.year_result >= 12
order by st.year_result DESC;

-- Exo 2.6.6
select professor_name, section_name, course_name, course_ects
from professor p
left join course c on c.professor_id = p.professor_id
inner join section s on p.section_id = s.section_id
order by course_name, course_ects DESC;

-- Exo 2.6.7
select p.professor_id, sum(course_ects) as "ECTS_TOT"
from professor p
left join course c on c.professor_id = p.professor_id
group by p.professor_id
order by "ECTS_TOT" DESC;

-- Exo 2.6.8
select p.professor_surname, p.professor_name, 'P' as "Catégorie"
from professor p
where length(professor_name) > 8
UNION
select s.first_name, s.last_name, 'S' as "Catégorie"
from student s
where length(last_name) > 8;

-- Exo 2.6.9
select s.section_id
from section s
EXCEPT
select p.section_id
from professor p;