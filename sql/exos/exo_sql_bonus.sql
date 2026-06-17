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

-- Exo 2.2.10
select norder
from porder
where norder not in (
select norder from detail
where npro in (
select npro
from product
where label like '%SAPIN%')
)
or norder in (
select norder from detail
where npro in (
select npro
from product
where label like '%ACIER%')
)
order by norder;

-- Exo 2.3 - Group by
-- Exo 2.3.1
select cat, sum(account), avg(account), count(ncli)
from client 
group by cat

-- Exo 2.3.2
select locality, sum(account), avg(account), count(ncli)
from client 
group by locality

-- Exo 2.3.3
select locality, avg(account)
from client 
where cat = 'C1' and locality in ('Namur', 'Poitiers')
group by locality

-- Exo 2.4 - Joins
-- Exo 2.4.1
select norder, name, locality
from porder po
inner join client c on c.ncli = po.ncli;

-- Exo 2.4.2
select po.norder, sum(qorder * price) as "Amount"
from porder po
inner join detail d on po.norder = d.norder
inner join product p on p.npro = d.npro
group by po.norder
order by "Amount" DESC;

-- Exo 2.4.4
select c.locality, c.cat, count(distinct po.norder), sum(qorder * price)
from porder po
inner join client c on c.ncli = po.ncli
inner join detail d on po.norder = d.norder
inner join product p on p.npro = d.npro
group by c.locality, c.cat;
-- Distinct nécessaire car sinon compte des doublons à cause de la table détails qui est embarquée
-- Quand on fait des jointures, l'unité de ligne est celle de la plus "basse" many dans les relations : 
-- ex. si client et order, order car client peut avoir plusieurs orders ; si client, order, détail, 
-- alors détail, car many de order qui est many de client

-- Exo 2.4.6
select p.label, c.locality, sum(qorder)
from porder po
inner join client c on c.ncli = po.ncli
inner join detail d on po.norder = d.norder
inner join product p on p.npro = d.npro
group by p.label, c.locality
having sum(qorder) > 500;