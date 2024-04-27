CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    registration_date VARCHAR(255),
    address VARCHAR(255),
    role VARCHAR(255),
    telephone VARCHAR(255),
    email VARCHAR(255));
INSERT INTO users (id, address, email, first_name, last_name, registration_date, role, telephone, username) VALUES 
(1, 'Didlaukio 59', 'example@example.com', 'Edvinas', 'Gerdvila', '2024-03-04', 'user', '123456789', 'Geed');
