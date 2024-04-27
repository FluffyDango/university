-- Show all my apointments (patient id = 1)
SELECT doc_name, doc_surname, start_time, end_time FROM doctor, timeslot WHERE doc_id = doc_id_slot AND pat_id_slot = 1;

-- Show all my time slots

SELECT slot_date, start_time, end_time FROM timeslot WHERE doc_id_slot = 1;

-- Show all my free time slots / show doctors free time slots

SELECT slot_date, start_time, end_time FROM timeslot WHERE doc_id_slot = 1 AND pat_id_slot is NULL;

-- Show all my taken time slots (doc id 1)

SELECT slot_date, start_time, end_time, pat_name, pat_surname FROM timeslot, patient WHERE pat_id_slot = pat_id AND doc_id_slot = 1;

-- Show all my patient card entries

SELECT slot_date, entry_text  FROM  patient_card_entry, visit, timeslot WHERE visit_id_entry =
visit_id AND slot_id_visit = slot_id AND pat_id_entry = 1;

-- Show all patient card entries

SELECT pat_name, pat_surname, slot_date, entry_text  FROM  patient_card_entry, visit, timeslot, patient WHERE visit_id_entry =
visit_id AND slot_id_visit = slot_id AND pat_id = pat_id_entry AND pat_id_entry = 1;