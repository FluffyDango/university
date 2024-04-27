import React from 'react';
import Navbar from '../../../../../components/navigation/navbar'
import styles from './prescriptions.module.css';

const Page: React.FC = () => {
  const prescriptions = [
    {
      patient: "John Johnson",
      medication: "Antidepressants 'StopPain'",
      dosage: '50mg',
      frequency: 'Once daily',
    },
    {
      patient: "Johnny Sinister",
      medication: "Testosterone booster 'BoostT'",
      dosage: '500mg',
      frequency: 'Once daily',
    },
  ];

  return (
    <>
      <Navbar navbarType="doctor" />
      <div className={styles.historyContainer}>
        <div className={styles.header}>
          <h1 className={styles.boldTitle}>Issued Prescriptions:</h1>
        </div>

        <main className={styles.mainContent}>
          {prescriptions.map((prescription, index) => (
            <section key={index} className={styles.card}>
              <h3 className={styles.boldTitle}>Prescription for {prescription.patient}:</h3>
              <p>Medication: {prescription.medication}</p>
              <p>Dosage: {prescription.dosage}</p>
              <p>Frequency: {prescription.frequency}</p>
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