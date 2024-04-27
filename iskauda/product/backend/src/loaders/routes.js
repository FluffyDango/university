import patientModule from '../components/patient/patient.module.js';
import doctorModule from '../components/doctor/doctor.module.js';
import appointmentModule from '../components/appointment/appointment.module.js';

export default (app) => {
  app.use('/patients', patientModule.router);
  app.use('/doctors', doctorModule.router);
  app.use('/appointment', appointmentModule.router);
};