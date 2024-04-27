import execute from '../../database.js';

class appointmentService {
    createAppointment = async (appointment) => {
        const requiredProperties = ['doc_id', 'pat_id', 'app_date', 'app_time'];
        for (const property of requiredProperties) {
            if (!appointment.hasOwnProperty(property)) {
                throw new Error(`Missing required property ${property}`);
            }
        }
        const { doc_id, pat_id, app_date, app_time } = appointment;

        const [checkres, _] = await execute(`
            SELECT doc_id, pat_id, app_date, app_time FROM appointment
            WHERE doc_id = ? AND pat_id = ? AND app_date = ? AND app_time = ?;
            `, [doc_id, pat_id, app_date, app_time]);
        if (checkres.length != 0) return JSON.stringify({ message: 'Appointment already exists' });

        const [results, fields] = await execute(`
            INSERT INTO appointment (doc_id, pat_id, app_date, app_time)
            VALUES (?, ?, ?, ?);
            `, [doc_id, pat_id, app_date, app_time]);
        if (results.length == 0) return JSON.stringify({ message: 'Appointment not created' });
        return JSON.stringify({ success: true });
    }

    getAppointments = async (id) => {
        if (!id) return JSON.stringify({ message: 'Missing required parameter: pat_id' });
        
        const [results, fields] = await execute(`
        SELECT doc_name, doc_surname, level, start_time, slot_date FROM doctor, timeslot 
        WHERE doc_id = doc_id_slot AND pat_id_slot = ?;
            `, [id]);
        // if (results.length == 0) return JSON.stringify({ message: 'Could not find any appointments' });
        return JSON.stringify(results);
    }
}

export default appointmentService;