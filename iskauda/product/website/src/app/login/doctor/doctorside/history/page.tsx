import React from 'react';
import Navbar from '../../../../components/navigation/navbar';
import styles from './history.module.css';

const historyData = [
  {
    patient: 'Jeff Jeffer',
    date: '2023-01-20',
    time: '09:30',
    diagnosis: 'High blood pressure',
    treatment: 'Recommended starting a healthy vegetarian diet.',
  },
  {
    patient: 'Olaf Olafson',
    date: '2022-12-15',
    time: '11:00',
    diagnosis: 'Routine Dental Check-up',
    treatment: 'Recommended cleaning teeth 2x a day.',
  },
  {
    patient: 'Richard Richardson',
    date: '2022-11-10',
    time: '15:45',
    diagnosis: 'Annual Blood Work',
    treatment: 'Everything looks great.',
  },
];

const Page: React.FC = () => {
  return (
    <>
      <Navbar navbarType="doctor" />
      <div className={styles.historyContainer}>
        <div className={styles.header}>
          <h1 className={styles.boldTitle}>Patient Consultation History:</h1>
        </div>

        <main className={styles.mainContent}>
          {historyData.map((record, index) => (
            <section key={index} className={styles.card}>
              <h3 className={styles.boldTitle}>Past Appointment:</h3>
              <p>Patient: {record.patient}</p>
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