import React from 'react';
import Navbar from '../../../../components/navigation/navbar';
import Link from 'next/link';
import styles from './profile.module.css';

const clientProfileData = {
  patientInfo: {
    name: 'Kevin Pavlov',
    dob: '2000-01-05',
    patientNumber: '15552125122',
    familyDoctor: 'Svetlana Alexeeva'
  },
  futureAppointment: {
    doctor: 'Peter Peterson',
    speciality: 'Cardiologist',
    date: '2024-04-20',
    time: '10:00',
    reason: 'Annual Heart Check-up'
  },
  pastAppointment: {
    doctor: 'John Borsch',
    speciality: 'General Practitioner',
    date: '2023-01-20',
    time: '10:00',
    diagnosis: 'High blood pressure',
    treatment: 'Recommended lifestyle changes and regular exercise.'
  },
  electronicPrescriptions: [
    "Antidepressants 'StopPain'",
    "Testosterone booster 'BoostT'"
  ]
};

const Page: React.FC = () => {
  return (
    <>
      <Navbar navbarType="client" />
      <div className={styles.profileContainer}>
        <aside className={styles.sidebar}>
          <h3 className={styles.boldTitle}>Patient Profile:</h3>
          <p>{clientProfileData.patientInfo.name}, {clientProfileData.patientInfo.dob}</p>
          <p>Patient Number: {clientProfileData.patientInfo.patientNumber}</p>
          <p>Family Doctor: {clientProfileData.patientInfo.familyDoctor}</p>
          <Link href="/login/client/clientside/profile/PatientDetails" passHref>
            <button style={{color: "black", fontWeight: "bold"}}>Show All</button>
          </Link>
        </aside>
        
        <main className={styles.mainContent}>
          <section className={styles.card}>
            <h3 className={styles.boldTitle}>Future Appointment:</h3>
            <p>Doctor: {clientProfileData.futureAppointment.doctor}</p>
            <p>Level: {clientProfileData.futureAppointment.speciality}</p>
            <p>Date: {clientProfileData.futureAppointment.date}</p>
            <p>Time: {clientProfileData.futureAppointment.time}</p>
            <p>Reason for Visit: {clientProfileData.futureAppointment.reason}</p>
            <Link href="/login/client/clientside/appointments" passHref>
              <button style={{color: "red"}}>Show All</button>
            </Link>
          </section>
          
          <section className={styles.card}>
            <h3 className={styles.boldTitle}>Past Appointment:</h3>
            <p>Doctor: {clientProfileData.pastAppointment.doctor}</p>
            <p>Level: {clientProfileData.pastAppointment.speciality}</p>
            <p>Date: {clientProfileData.pastAppointment.date}</p>
            <p>Time: {clientProfileData.pastAppointment.time}</p>
            <h5>Diagnosis:</h5>
            <p>{clientProfileData.pastAppointment.diagnosis}</p>
            <h5>Treatment:</h5>
            <p>{clientProfileData.pastAppointment.treatment}</p>
            <Link href="/login/client/clientside/history" passHref>
              <button style={{color: "red"}}>Show All</button>
            </Link>
          </section>
          
          <article className={styles.info}>
            <h3 className={styles.boldTitle}>Electronic Prescriptions:</h3>
            {clientProfileData.electronicPrescriptions.map((prescription, index) => (
              <p key={index}>{prescription}</p>
            ))}
            <Link href="/login/client/clientside/profile/Prescriptions" passHref>
              <button style={{color: "red"}}>Show All</button>
            </Link>
          </article>
        </main>
      </div>

      <footer className={styles.footer}>
        <p>&copy; 2023 Hospital Portal. All rights reserved.</p>
      </footer>
    </>
  );
};

export default Page;