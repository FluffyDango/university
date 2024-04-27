import React from 'react';
import Navbar from '../../../../../components/navigation/navbar'
import styles from './prescriptions.module.css';

const page: React.FC = () => {
  const prescriptions = [
     {
          medication: "Antidepressants 'StopPain'",
          dosage: '50mg',
          frequency: 'Once daily',
          prescribedBy: 'Dr. Jeff Duraswami'
        },
        {
         medication: "Testosterone booster 'BoostT'",
         dosage: '500mg',
         frequency: 'Once daily',
         prescribedBy: 'Dr. Jeff Duraswami'
       },
  ];

  return (
    <>
      <Navbar navbarType="client" />
      <div className={styles.historyContainer}>
        <div className={styles.header}>
          <h1 className={styles.boldTitle}>My Prescriptions:</h1>
        </div>

        <main className={styles.mainContent}>
          {prescriptions.map((prescription, index) => (
            <section key={index} className={styles.card}>
              <h3 className={styles.boldTitle}>Prescription Details:</h3>
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

export default page;


