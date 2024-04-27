CREATE TABLE propertystorage (
    id SERIAL NOT NULL,
    path VARCHAR(1024) NOT NULL,
    name VARCHAR(100) NOT NULL,
    value TEXT
);

ALTER TABLE ONLY propertystorage
    ADD CONSTRAINT propertystorage_pkey PRIMARY KEY (id);

CREATE UNIQUE INDEX propertystorage_ukey
    ON propertystorage (path, name);

-- The propertystorage table is used to store properties for resources.
-- The properties are stored in a key-value pair.
-- Such as {DAV:}displayname = "My file.txt"