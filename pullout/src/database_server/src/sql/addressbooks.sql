CREATE TABLE addressbooks (
    id SERIAL NOT NULL,
    principaluri VARCHAR(255),
    displayname VARCHAR(255),
    uri VARCHAR(200),
    description TEXT,
    synctoken INTEGER NOT NULL DEFAULT 1
);

ALTER TABLE ONLY addressbooks
    ADD CONSTRAINT addressbooks_pkey PRIMARY KEY (id);

CREATE UNIQUE INDEX addressbooks_ukey
    ON addressbooks USING btree (principaluri, uri);

CREATE TABLE cards (
    id SERIAL NOT NULL,
    addressbookid INTEGER NOT NULL,
    carddata TEXT,
    uri VARCHAR(200),
    lastmodified INTEGER,
    etag VARCHAR(32),
    size INTEGER NOT NULL
);

ALTER TABLE ONLY cards
    ADD CONSTRAINT cards_pkey PRIMARY KEY (id);

CREATE UNIQUE INDEX cards_ukey
    ON cards USING btree (addressbookid, uri);

ALTER TABLE ONLY cards
    ADD CONSTRAINT cards_addressbookid_fkey FOREIGN KEY (addressbookid) REFERENCES addressbooks(id)
        ON DELETE CASCADE;

CREATE TABLE addressbookchanges (
    id SERIAL NOT NULL,
    uri VARCHAR(200) NOT NULL,
    synctoken INTEGER NOT NULL,
    addressbookid INTEGER NOT NULL,
    operation SMALLINT NOT NULL
);

ALTER TABLE ONLY addressbookchanges
    ADD CONSTRAINT addressbookchanges_pkey PRIMARY KEY (id);

CREATE INDEX addressbookchanges_addressbookid_synctoken_ix
    ON addressbookchanges USING btree (addressbookid, synctoken);

ALTER TABLE ONLY addressbookchanges
    ADD CONSTRAINT addressbookchanges_addressbookid_fkey FOREIGN KEY (addressbookid) REFERENCES addressbooks(id)
        ON DELETE CASCADE;

-- Add new addressbooks. The way you will use these addressbooks
-- in CardDav client is by specifying the url of the addressbook.
-- It would look like this:
-- http://localhost:8080/addressbooks/admin/contacts/
INSERT INTO addressbooks(principaluri, displayname, uri) VALUES
('principals/all', 'all', 'all'),
('principals/all', 'test', 'test'),
('principals/all', 'AnotherTest', 'AnotherTest');

INSERT INTO cards(addressbookid, carddata, uri, lastmodified, etag, size) VALUES
(1, 'BEGIN:VCARD
VERSION:3.0
FN:Piotr Jasinski
ORG:Mediaspektras
TEL:+37067604754
TITLE:Direktorius
END:VCARD', 'piotr.vcf', 0, '1234567890', 0);
