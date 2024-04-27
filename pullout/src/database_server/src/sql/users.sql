CREATE TABLE users (
    id SERIAL NOT NULL,
    username VARCHAR(50),
    digesta1 VARCHAR(32)
);

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);

CREATE UNIQUE INDEX users_ukey
    ON users USING btree (username);

-- digesta1 is the md5 hash of the string "username:realm:password"
-- Realm is the string "SabreDAV"
-- The password is "admin" for the admin. But we are not implementing password authentication
-- users will have empty digesta1
-- Or we will just not have users at all.
-- examples are made using php -r "echo md5('all:pullout:all');"
INSERT INTO users (username,digesta1) VALUES
('all', '3eb0f9122e0784e27fda377fda37e10e');
-- ('guest', 'b384a2802fac2d3493b13ed952114d9c');
-- ('admin',  '87fd274b7b6c01e48d7c2f965da8ddf7');