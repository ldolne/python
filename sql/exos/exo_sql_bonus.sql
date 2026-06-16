-- Exo bonus

-- Exo 2.1 - Basics

-- Exo 2.1.1
select ncli, name, locality 
from client
where cat = 'C1' and locality != 'Toulouse';


-- Exo 2.1.2
select ncli, name, account 
from client
where locality in ('Poitiers', 'Brussels') and account < 0;

-- Exo 2.1.3
select ncli, name, locality 
from client
where name < locality;

-- Exo 2.1.4
select ncli, locality 
from client
where locality in ('Lille', 'Namur');

-- Exo 2.1.5
select ncli, locality 
from client
where cat = 'C1' and locality != 'Namur';

-- Exo 2.1.6
select ncli, locality 
from client
where (cat in ('B1','C1') and locality not in ('Lille', 'Namur')) OR 
(cat not in ('B1','C1') and locality in ('Lille', 'Namur'));

-- Exo 2.2 - Subqueries
-- Exo 2.2.1
select ncli, name 
from client
where locality = 'Namur' and ncli not in (select ncli from porder)

-- Exo 2.2.1
select npro
from product
where label like '%SAPIN%' and npro in (select npro from detail);
order by npro