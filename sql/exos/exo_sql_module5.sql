-- Exos CUBE et ROLLUP
-- Exo 2.5.1
/*
FAUX. 
ROLLUP est hiérarchique et unidirectionnel : il respecte l'ordre des colonnes 
listées et agrège progressivement en retirant une colonne à la fois, en
partant de la droite. 
La hiérarchie se lit donc de gauche à droite — la colonne
la plus à gauche est le niveau le plus élevé de la hiérarchie.
Le ROLLUP crée les totaux en partant de droite à gauche.
ROLLUP(a, b, c) génère exactement ces ensembles de regroupement :
(a, b, c)
(a, b)
(a)
()
Il ne produit JAMAIS, par exemple, (b, c) ou (b) seuls — contrairement à CUBE
qui explore toutes les combinaisons. C'est en ce sens que ROLLUP va « dans une
seule direction ».
*/

-- Exo 2.5.2
/*
FAUX (à double titre).
Conceptuellement, ROLLUP génère les ensembles du MOINS agrégé (le détail
complet : pays, ville) vers le PLUS agrégé (le total général ()) — donc
l'inverse de ce qui est affirmé.
Surtout : en PostgreSQL, AUCUN ordre des lignes n'est garanti sans une
clause ORDER BY explicite. La présentation « total en haut » ou « total en
bas » n'est jamais implicite ; il faut l'imposer soi-même.
*/

-- Exo 2.5.3
/*
FAUX.
CUBE produit PLUS de sous-totaux que ROLLUP, pas moins.
ROLLUP sur n colonnes  -> n + 1 ensembles de regroupement.
CUBE sur n colonnes     -> 2^n ensembles (toutes les combinaisons).
Exemple sur 2 colonnes (a, b) :
ROLLUP -> 3 ensembles : (a,b), (a), ()
CUBE   -> 4 ensembles : (a,b), (a), (b), ()
CUBE ajoute notamment le sous-total (b) seul, que ROLLUP ne produit pas.
*/

-- Exo 2.5.4
/*
FAUX.
Le nombre de groupes dépend DIRECTEMENT du nombre de colonnes : CUBE génère
2^n ensembles de regroupement, où n est le nombre de colonnes du CUBE.

1 colonne  -> 2^1 = 2 ensembles
2 colonnes -> 2^2 = 4 ensembles
3 colonnes -> 2^3 = 8 ensembles

Le résultat est donc tout sauf indépendant du nombre de colonnes.
*/

-- Exo 2.5.5
/*
FAUX.
CUBE (comme ROLLUP) s'applique à toutes les fonctions
d'agrégation standard : SUM, COUNT, AVG, MIN, MAX, etc. Ces opérateurs
modifient seulement la manière de regrouper les lignes ; ils n'imposent
aucune restriction sur la fonction d'agrégation utilisée.*/

-- Exo 2.5.6
select section_id, course_id, avg(year_result) as "Moyenne"
from student
where section_id in (1010,1320)
group by rollup (section_id, course_id)
order by section_id, course_id;

-- Exo 2.5.7
select section_id, course_id, avg(year_result) as "Moyenne"
from student
where section_id in (1010,1320)
group by cube (course_id,section_id)
order by section_id, course_id;