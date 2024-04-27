-- Doctor Table
CREATE TABLE IF NOT EXISTS doctor (
    doc_id INT AUTO_INCREMENT,
    doc_name VARCHAR(50),
    doc_surname VARCHAR(50),
    level VARCHAR(50),
    doc_username VARCHAR(50) UNIQUE,
    doc_password VARCHAR(50) NOT NULL,
    PRIMARY KEY (doc_id)
);

-- Patient Table
CREATE TABLE IF NOT EXISTS patient (
    pat_id INT AUTO_INCREMENT,
    pat_name VARCHAR(50),
    pat_surname VARCHAR(50),
    pat_username VARCHAR(50) UNIQUE,
    pat_password VARCHAR(50) NOT NULL,
    PRIMARY KEY (pat_id)
);

-- Timeslot Table
CREATE TABLE IF NOT EXISTS timeslot (
    slot_id INT AUTO_INCREMENT,
    slot_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    doc_id_slot INT NOT NULL,
    pat_id_slot INT,
    PRIMARY KEY (slot_id),
    CONSTRAINT fk_doc_id FOREIGN KEY (doc_id_slot) REFERENCES doctor(doc_id),
    CONSTRAINT fk_pat_id FOREIGN KEY (pat_id_slot) REFERENCES patient(pat_id)
);

-- Visit Table
CREATE TABLE IF NOT EXISTS visit (
    visit_id INT AUTO_INCREMENT,
    has_happened BOOLEAN DEFAULT FALSE,
    slot_id_visit INT NOT NULL,
    PRIMARY KEY (visit_id),
    CONSTRAINT fk_timeSlotId FOREIGN KEY (slot_id_visit) REFERENCES timeslot(slot_id)
);

-- PatientCardEntry Table
CREATE TABLE IF NOT EXISTS patient_card_entry (
    entry_id INT AUTO_INCREMENT,
    entry_text VARCHAR(600) NOT NULL,
    pat_id_entry INT NOT NULL,
    visit_id_entry INT NOT NULL,
    PRIMARY KEY (entry_id),
    CONSTRAINT fk_patients_id FOREIGN KEY (pat_id_entry) REFERENCES patient(pat_id),
    CONSTRAINT fk_visit_id FOREIGN KEY (visit_id_entry) REFERENCES visit(visit_id)
);
