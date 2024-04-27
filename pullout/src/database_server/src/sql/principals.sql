CREATE TABLE principals (
    id SERIAL NOT NULL,
    uri VARCHAR(200) NOT NULL,
    email VARCHAR(80),
    displayname VARCHAR(80),
    vcardurl VARCHAR(255)
);

ALTER TABLE ONLY principals
    ADD CONSTRAINT principals_pkey PRIMARY KEY (id);

CREATE UNIQUE INDEX principals_ukey
    ON principals USING btree (uri);

CREATE TABLE groupmembers (
    id SERIAL NOT NULL,
    principal_id INTEGER NOT NULL,
    member_id INTEGER NOT NULL
);

ALTER TABLE ONLY groupmembers
    ADD CONSTRAINT groupmembers_pkey PRIMARY KEY (id);

CREATE UNIQUE INDEX groupmembers_ukey
    ON groupmembers USING btree (principal_id, member_id);

ALTER TABLE ONLY groupmembers
    ADD CONSTRAINT groupmembers_principal_id_fkey FOREIGN KEY (principal_id) REFERENCES principals(id)
        ON DELETE CASCADE;

ALTER TABLE ONLY groupmembers
    ADD CONSTRAINT groupmembers_member_id_id_fkey FOREIGN KEY (member_id) REFERENCES principals(id)
        ON DELETE CASCADE;

-- Principals are the users and groups that can be used in the ACL system.
-- It is the authentication system and without a principal you cannot own a resource.
-- We are not using authentication so we will have default principals.
INSERT INTO principals (uri,displayname) VALUES
('principals/all', 'All users');
-- ('principals/admin','Administrator'),
-- ('principals/users', 'Normal users'),
-- ('principals/groups', 'Groups');