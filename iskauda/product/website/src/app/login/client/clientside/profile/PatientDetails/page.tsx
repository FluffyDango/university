import React from 'react';
import Navbar from '../../../../../components/navigation/navbar';
import styles from './patientDetails.module.css';

const patientDetails = {
  fullName: 'Kevin Pavlov',
  patientNumber: '15552125122',
  patientId: '15552125122',
  dob: '2000-01-05',
  familyDoctor: 'Svetlana Alexeeva',
  age: 23,
  ssn: '50102152100',
  sex: 'Male',
  address: 'Cosmos 540-24',
  phoneNumber: '+441241522124'
};

const Page: React.FC = () => {
  return (
    <>
      <Navbar navbarType="client" />
      <div className={styles.patientDetailsContainer}>
        <div className={styles.title}>Patient Details:</div>
        <div className={styles.card}>
          <p><span className={styles.boldTitle}>Full Name:</span> {patientDetails.fullName}</p>
          <p><span className={styles.boldTitle}>Patient Number:</span> {patientDetails.patientNumber}</p>
          <p><span className={styles.boldTitle}>DOB:</span> {patientDetails.dob}</p>
          <p><span className={styles.boldTitle}>Family Doctor:</span> {patientDetails.familyDoctor}</p>
          <p><span className={styles.boldTitle}>Age:</span> {patientDetails.age}</p>
          <p><span className={styles.boldTitle}>SSN:</span> {patientDetails.ssn}</p>
          <p><span className={styles.boldTitle}>Sex:</span> {patientDetails.sex}</p>
          <p><span className={styles.boldTitle}>Address:</span> {patientDetails.address}</p>
          <p><span className={styles.boldTitle}>Phone Number:</span> {patientDetails.phoneNumber}</p>
        </div>
        <footer className={styles.footer}>
          <p>&copy; 2023 Hospital Portal. All rights reserved.</p>
        </footer>
      </div>
    </>
  );
};

export default Page;