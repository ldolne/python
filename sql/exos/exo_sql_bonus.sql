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
order by ncli asc;

-- Exo 2.2.2
select npro
from product
where label like '%SAPIN%' and npro in (select npro from detail);
order by npro

-- inversé
select distinct npro
from detail
where npro in (select npro from product where label like '%SAPIN%');

-- Exo 2.2.3
select ncli
from client
where account >= 0 OR ncli in
(select distinct ncli 
from porder)
order by ncli; -- account < 0 pas nécessaire car déjà compris suite à OR et account >= 0

-- Exo 2.2.4
-- not (x and y)
select ncli
from client
where ncli not in
(select c.ncli 
from client c
where cat in ('B1','C1')) or ncli not in (select c.ncli 
from client c
where locality in ('Lille','Namur'))
order by ncli;
-- Not x OR not y
select NCLI
from client
where NCLI not in (
select ncli from client
where (cat in ('B1', 'C1')) and (locality in ('Lille', 'Namur'))
)
order by ncli;

-- Exo 2.2.5
select p.npro, p.label
from product p
where label like '%SAPIN%' and 
npro not in (select d.npro
from detail d
inner join porder po on d.norder = po.norder
inner join client c on po.ncli = c.ncli
where locality != 'Toulouse')
and npro in (select d.npro
from detail d
inner join porder po on d.norder = po.norder
inner join client c on po.ncli = c.ncli
where locality = 'Toulouse');

-- Avec full subqueries
select p.npro, p.label
from product p
where label like '%SAPIN%' 
	and npro not in (select npro
					from detail 
					where norder in (select norder
									from porder
									where ncli in (select ncli
													from client
													where locality = 'Toulouse')))
and npro not in (select npro
				from detail 
				where norder in (select norder
								from porder
								where ncli in (select ncli
											from client
											where locality != 'Toulouse')))

-- Avec except
select p.npro, p.label
from product p
where label like '%SAPIN%' and 
npro in 
(select d.npro
from detail d
inner join porder po on d.norder = po.norder
inner join client c on po.ncli = c.ncli
where locality = 'Toulouse'
except 
select d.npro
from detail d
inner join porder po on d.norder = po.norder
inner join client c on po.ncli = c.ncli
where locality != 'Toulouse');

-- Exo 2.2.6
select count(norder) as "nbOrders"
from porder
where norder in (
select po.norder
from detail d
inner join porder po on d.norder = po.norder
inner join product p on d.npro = p.npro
where p.label like '%ACIER%'
);

-- Exo 2.2.7
select distinct locality
from client
where ncli in (select ncli
				from porder
				where date_part('year', ordermoment) = '2008' and 
				date_part('month', ordermoment) = '12')
order by locality ASC;

-- Exo 2.2.8
select npro, label
from product
where npro not in (select d.npro
					from detail d
					inner join porder po on d.norder = po.norder
					where date_part('year', ordermoment) = '2008' and 
					date_part('month', ordermoment) = '12');
-- Full subqueries
select npro, label
from product
where npro not in (select npro
					from detail
					where norder in (select norder
										from porder
										where date_part('year', ordermoment) = '2008' and 
										date_part('month', ordermoment) = '12'));

-- Exo 2.2.9
select distinct locality
from client
where locality not in(
select locality
from client
where ncli not in(select ncli
from porder));

-- Avec join et null
select locality
from client
where locality not in (select distinct locality
from porder p
right join client c
on p.ncli = c.ncli
where p.norder is null
group by locality);

select locality
from client
where ncli not in(select ncli
from porder);

select c.ncli, c.locality
from porder po
inner join client c on po.ncli = c.ncli;

select locality
from client
group by locality 
having count(ncli) >= all(
select count(*)
from client
where ncli in(
-- Clients qui ont commandé
select c.ncli
from client c
inner join porder po on c.ncli = po.ncli)
group by locality);

-- other
select locality
from client
group by locality 
having count(ncli) = all(
select count(*)
from client
where ncli in(
-- Clients qui ont commandé
select c.ncli
from client c
inner join porder po on c.ncli = po.ncli)
group by locality);

-- ddd
select locality, string_agg(c.ncli, ', '), count(norder)
from client c
inner join porder po on c.ncli = po.ncli
group by locality, c.ncli;
select count(ncli)
from client
group by locality ;

-- Exo 2.2.10
select norder
from porder
where norder not in (
select norder from detail
where npro in ( -- not in pas possible ici, car récupérerait les commandes avec des lignes de détails sans sapin, mais la même commande pourrait avoir une ligne détail sapin non sélectionnée ici
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