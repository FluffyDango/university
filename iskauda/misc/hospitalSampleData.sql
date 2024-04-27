-- Doctor Table
INSERT INTO doctor (doc_name, doc_surname, level, doc_username, doc_password) VALUES
('Dovydas', 'Daktarauskas', 'Cardiologist', 'doda1234', 'password'),
('Rimvydas', 'Bozena', 'Neurosurgeon', 'ribo1234', 'password'),
('Karolis', 'Rimtis', 'Family Doctor', 'kari1234', 'password'),
('Antanas', 'Burokas', 'Family Doctor', 'anbu1234', 'password'),
('Rima', 'Rimaite', 'Dermatologist', 'riri1234', 'password');

-- Patient Table
INSERT INTO patient (pat_name, pat_surname, pat_username, pat_password) VALUES 
('Jomas', 'Daniunas','joda1234', 'password'),
('Tomas', 'Tomauskas', 'toto1234', 'password'),
('Rokas', 'Rokauskas', 'roro1234', 'password'),
('Karolis', 'Bananauskas', 'kaba1234', 'password'),
('Roma', 'Pastataite', 'ropa1234', 'password');

-- TimeSlot Table
INSERT INTO timeslot (slot_date, start_time, end_time, doc_id_slot) VALUES
('2023-11-20', '10:00:00', '11:00:00', 1),
('2023-11-21', '10:00:00', '11:00:00', 1),
('2023-12-21', '10:00:00', '11:00:00', 1),
('2023-12-21', '11:15:00', '11:30:00', 1),
('2023-12-10', '12:00:00', '13:00:00', 3),
('2023-12-10', '12:00:00', '13:00:00', 4),
('2023-12-26', '13:00:00', '13:45:00', 5),
('2023-12-26', '14:00:00', '14:45:00', 5),
('2023-12-26', '15:00:00', '15:45:00', 5),
('2023-12-26', '16:00:00', '16:45:00', 5),
('2023-12-26', '17:00:00', '17:45:00', 5),
('2023-12-10', '13:15:00', '14:00:00', 3),
('2023-12-10', '13:15:00', '14:00:00', 4),
('2023-12-10', '14:15:00', '15:00:00', 3),
('2023-12-10', '14:15:00', '15:00:00', 4),
('2023-12-10', '16:15:00', '17:00:00', 3),
('2023-12-10', '16:15:00', '17:00:00', 4),
('2023-12-15', '12:00:00', '18:00:00', 2),
('2023-12-18', '12:00:00', '18:00:00', 2),
('2023-12-21', '12:00:00', '18:00:00', 2),
('2023-12-28', '12:00:00', '18:00:00', 2);


INSERT INTO timeslot (slot_date, start_time, end_time, doc_id_slot, pat_id_slot) VALUES
('2023-12-21', '10:00:00', '11:00:00', 2, 1),
('2023-12-10', '15:15:00', '16:00:00', 3, 1),
('2023-12-10', '15:15:00', '16:00:00', 4, 2);

-- Visit Table
INSERT INTO visit (has_happened, slot_id_visit) VALUES
(TRUE, 1),
(TRUE, 2);

-- PatientCardEntry Table
INSERT INTO patient_card_entry (pat_id_entry, entry_text, visit_id_entry) VALUES
(1, 'He is very healthy', 2),
(1, 'We took a blood sample', 1);