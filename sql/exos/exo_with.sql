--Cas d'usages du WITH

/*
1) nommer une subquery pour plus de lisibilité
2) réutiliser plusieurs fois la subquery sans devoir réécrire toutes l'expression
3) chainer des étapes de transformation
	etape 1 --> with 1
		2 --> with 2
		3 --> with 3
4) CTE récursive : une CTE peut s'appeler elle meme (expl hierarchie, générer des nombres, arbre de catégorie (produit parent d'autres produits), …)
*/

WITH RECURSIVE hierarchie AS (
    -- Cas de base : l'employé de départ
    SELECT id, name, manager_id, 1 AS niveau
    FROM employees
    WHERE name = 'Heidi'
    UNION ALL
    -- Cas récursif : on remonte vers le manager
    SELECT e.id, e.name, e.manager_id, h.niveau + 1
    FROM employees e
    INNER JOIN hierarchie h ON e.id = h.manager_id
)
SELECT name, niveau FROM hierarchie;

-- with nom as materialized (…) force la matérialisation (mise en cache)

-- Stocker une table with

/*1) Vue matérialisée — CREATE MATERIALIZED VIEW nom AS <requête>. Techniquement c'est une « vue », 
mais contrairement à la vue classique elle stocke physiquement le résultat. 
Accessible par son nom partout, rafraîchissable avec REFRESH MATERIALIZED VIEW nom.
*/

CREATE VIEW hierarchie_managers AS
WITH RECURSIVE h AS (
    -- Cas de base : chaque employé est son propre point de départ
    SELECT id, name, manager_id, 1 AS niveau,
           id   AS depart_id,
           name AS depart_name
    FROM employees
    UNION ALL
    -- Cas récursif : on remonte vers le manager
    SELECT e.id, e.name, e.manager_id, h.niveau + 1,
           h.depart_id, h.depart_name
    FROM employees e
    INNER JOIN h ON e.id = h.manager_id
)
SELECT depart_name, name, niveau FROM h;

/* 2) Table via CREATE TABLE AS — CREATE TABLE nom AS <requête>. 
Crée une vraie table persistante contenant le snapshot des données au moment de la création. 
C'est figé : ça ne se met pas à jour si les données sources changent. 
On peut ensuite l'utiliser par son nom comme n'importe quelle table.*/

/* 3) Fonction — CREATE FUNCTION nom() RETURNS TABLE(...) ... ou RETURNS SETOF. 
Encapsule la logique, appelable par son nom (SELECT * FROM nom()), paramétrable. 
C'est l'équivalent le plus proche d'une « requête nommée réutilisable » avec de la logique dedans.
*/ 

/*
-------------------------------
DDL + INSERT TABLE HIERARCHIE |
-------------------------------

CREATE TABLE employees (
    id          INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    manager_id  INTEGER,
    CONSTRAINT fk_manager FOREIGN KEY (manager_id) REFERENCES employees (id)
);

INSERT INTO employees (name, manager_id) VALUES
    ('Diana',   NULL),   -- id = 1  (PDG)
    ('Charlie', 1),      -- id = 2
    ('Bob',     2),      -- id = 3
    ('Alice',   3),      -- id = 4  (point de départ de la requête)
    ('Eve',     1),      -- id = 5
    ('Frank',   2),      -- id = 6
    ('Grace',   3),      -- id = 7
    ('Heidi',   5),      -- id = 8
    ('Ivan',    5),      -- id = 9
    ('Judy',    4),      -- id = 10
    ('Mallory', 4),      -- id = 11
    ('Niaj',    6),      -- id = 12
    ('Olivia',  7),      -- id = 13
    ('Peggy',   8);      -- id = 14
*/