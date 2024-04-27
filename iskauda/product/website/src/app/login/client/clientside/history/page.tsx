import React from 'react';
import Navbar from '../../../../components/navigation/navbar';
import styles from './history.module.css';

const historyData = [
  {
    doctor: 'John Borsch',
    speciality: 'General Practitioner',
    date: '2023-01-20',
    time: '10:00',
    diagnosis: 'High blood pressure',
    treatment: 'Recommended lifestyle changes and regular exercise.'
  },
  {
    doctor: 'Hannah Robbins',
    speciality: 'Dentist',
    date: '2022-12-15',
    time: '14:00',
    diagnosis: 'Routine Dental Check-up',
    treatment: 'Cleaning scheduled in six months.'
  },
  {
    doctor: 'Arun Hindi',
    speciality: 'Lab Technician',
    date: '2022-11-10',
    time: '09:00',
    diagnosis: 'Annual Blood Work',
    treatment: 'No immediate concerns; maintain a healthy diet.'
  }
];

const Page: React.FC = () => {
  return (
    <>
      <Navbar navbarType="client" />
      <div className={styles.historyContainer}>
        <div className={styles.header}>
          <h1 className={styles.boldTitle}>My History:</h1>
        </div>

        <main className={styles.mainContent}>
          {historyData.map((record, index) => (
            <section key={index} className={styles.card}>
              <h3 className={styles.boldTitle}>Past Appointment:</h3>
              <p>Doctor: {record.doctor}</p>
              <p>Level: {record.speciality}</p>
              <p>Date: {record.date}</p>
              <p>Time: {record.time}</p>
              <h5>Diagnosis:</h5>
              <p>{record.diagnosis}</p>
              <h5>Treatment:</h5>
              <p>{record.treatment}</p>
            </section>
          ))}
        </main>
      </div>

      <footer className={styles.footer}>
        <p>&copy; 2023 Hospital Portal. All rights reserved.</p>
      </footer>
    </>
  );
};

export default Page;