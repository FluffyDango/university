CREATE TABLE USERS(
    pid BigSerial Primary Key ,
    first_name varchar(100),
    last_name varchar(100),
    login varchar(40),
    password varchar(30)
);