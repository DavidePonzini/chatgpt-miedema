queries = {
    '4.2': 'List all IDs & names of customers living in Eindhoven.',
    '4.3': 'List all pairs of customer IDs who live on a street with the same name but in a different city.',
    '4.4': 'List all customer IDs, dates and quantities of transactions containing products named Apples.',
    '4.5': 'Find the names of all inventory items that have a higher unit price than Bananas.',
    '4.6': 'Return a list of the number of stores per city.',
    '4.7': 'Return the stores table ordered alphabetically on city.',
    '4.9': 'A store-chain consists of at least two stores with the same name but different IDs. Find the names of the store-chains that on average sell product in quantities of more than 4.'
}

tables = '''BEGIN TRANSACTION;

drop schema if exists "miedema" cascade;

create schema "miedema";
set search_path to "miedema";

CREATE TABLE customer(
    cID DECIMAL(5,0) PRIMARY KEY,
    cName VARCHAR(255) NOT NULL,
    street VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL
);

CREATE TABLE store(
    sID DECIMAL(5,0) PRIMARY KEY,
    sName VARCHAR(255) NOT NULL,
    street VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL
);

CREATE TABLE product(
    pID DECIMAL(5,0) PRIMARY KEY,
    pName VARCHAR(255) NOT NULL,
    suffix VARCHAR(255)
);

CREATE TABLE shoppinglist(
    cID DECIMAL(5,0),
    pID DECIMAL(5,0),
    quantity DECIMAL(10,0) NOT NULL,
    date DATE NOT NULL,
    PRIMARY KEY(cID, pID)
);

CREATE TABLE transaction(
    tID DECIMAL(5,0),
    cID DECIMAL(5,0) NOT NULL,
    sID DECIMAL(5,0) NOT NULL,
    pID DECIMAL(5,0),
    date DATE NOT NULL,
    quantity DECIMAL(10,0) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    PRIMARY KEY(tID, pID)
);

CREATE TABLE inventory(
    sID DECIMAL(5,0),
    pID DECIMAL(5,0),
    date DATE NOT NULL,
    quantity DECIMAL(10) NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY(sID, pID, date)
);

INSERT INTO customer VALUES
(0, 'Noah', 'Koestraat', 'Ultrecht'),
(1, 'Sem', 'Rozemarijnstraat', 'Breda'),
(2, 'Lucas', 'Oude Leliestraat', 'Amsterdam'),
(3, 'Daan',  'Kalverstraat', 'Amsterdam');

INSERT INTO store VALUES
(0, 'Coop', 'Kalverstraat', 'Amsterdam'),
(1, 'Lidl', 'Hoogstraat', 'Utrecht'),
(2, 'Lidl', 'Molenstraat', 'Eindhoven'),
(3, 'Hoogvliet', 'Rozemarijnstraat', 'Breda'),
(4, 'Sligro', 'Stationsplein', 'Breda');

INSERT INTO transaction VALUES
(0, 0, 4, 3, '2020-05-12', 5, .4),
(1, 0, 4, 1, '2020-05-13', 2, .65),
(2, 2, 0, 4, '2020-05-13', 2, 1.3),
(3, 3, 0, 1, '2020-05-15', 1, .67);

INSERT INTO shoppinglist VALUES
(1, 2, 1, '2020-05-13'),
(1, 3, 6, '2020-05-13'),
(3, 1, 2, '2020-05-15');

INSERT INTO inventory VALUES
(0, 1, '2020-05-15', 55, .55),
(0, 2, '2020-05-15', 32, 2.3),
(1, 4, '2020-05-15', 12, 1.8),
(1, 1, '2020-05-15', 46, .6);

INSERT INTO product VALUES
(1, 'Milk', '""'),
(2, 'Mushrooms', '""'),
(3, 'Apples', '""'),
(4, 'Tea', '""'),
(5, 'Banana', '""');

COMMIT;'''