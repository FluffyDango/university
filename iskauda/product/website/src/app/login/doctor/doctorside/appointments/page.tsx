import React from 'react';
import Navbar from '../../../../components/navigation/navbar'
import styles from './appointments.module.css';

const appointmentsData = [
  {
    patient: 'Peter Peterson',
    date: '2024-04-20',
    time: '10:00',
  },
  {
    patient: 'Jordan Jordanson',
    date: '2023-12-29',
    time: '14:00',
  },
];

const Page: React.FC = () => {
  return (
    <>
      <Navbar navbarType="doctor" />
      <div className={styles.appointmentsContainer}>
        <h1 className={styles.title}>Upcoming Appointments:</h1>
        {appointmentsData.map((appointment, index) => (
          <div key={index} className={styles.card}>
            <h3 className={styles.boldTitle}>Appointment Details:</h3>
            <p>Patient: {appointment.patient}</p>
            <p>Date: {appointment.date}</p>
            <p>Time: {appointment.time}</p>
          </div>
        ))}
        <footer className={styles.footer}>
          <p>&copy; 2023 Hospital Portal. All rights reserved.</p>
        </footer>
      </div>
    </>
  );
};

export default Page;