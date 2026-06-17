-- Bonus
-- Display all orders that do not include the product PA60
select norder
from porder
where norder not in 
(select norder from detail where npro = 'PA60');

-- Celle-ci est fausse !
-- On récupère des lignes de détails d'une commande qui, pour cette ligne, 
-- ne comprennent pas 'PA60', mais pour une autre ligne de détail bien
select norder
from porder
where norder in 
(select norder from detail where npro != 'PA60');