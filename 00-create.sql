BEGIN TRANSACTION;

drop schema if exists "miedema" cascade;

create schema "miedema";
set search_path to "miedema";

CREATE TABLE customer(
    cID DECIMAL(5,0) PRIMARY KEY,
    cName VARCHAR(255),
    street VARCHAR(255),
    city VARCHAR(255)
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

CREATE TABLE purchase(
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


COMMIT;