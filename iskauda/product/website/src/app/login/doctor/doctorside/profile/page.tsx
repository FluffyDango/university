import React from 'react';
import Navbar from '../../../../components/navigation/navbar';
import Link from 'next/link';
import styles from './profile.module.css';

const profileData = {
  doctorInfo: {
    name: 'Olfried Oleksandrovich',
    dob: '1956-02-22',
    licenseNumber: '16218901',
    qualification: 'Urologist'
  },
  upcomingAppointment: {
    patient: 'Peter Peterson',
    date: '2024-04-20',
    time: '10:00',
    reason: 'Check-up'
  },
  lastConsultation: {
    patient: 'Jeff Jeffer',
    date: '2023-01-20',
    time: '09:30',
    diagnosis: 'High blood pressure',
    treatment: 'Recommended starting a healthy vegetarian diet.'
  },
  lastIssuedPrescription: {
    patient: 'John Johnson',
    medication: "Antidepressants 'StopPain'"
  }
};

const Page: React.FC = () => {
  return (
    <>
      <Navbar navbarType="doctor" />
      <div className={styles.profileContainer}>
        <aside className={styles.sidebar}>
          <h3 className={styles.boldTitle}>Doctor Profile:</h3>
          <p>{profileData.doctorInfo.name}, {profileData.doctorInfo.dob}</p>
          <p>Doctor License Number: {profileData.doctorInfo.licenseNumber}</p>
          <p>Level: {profileData.doctorInfo.qualification}</p>
        </aside>
        
        <main className={styles.mainContent}>
          <section className={styles.card}>
            <h3 className={styles.boldTitle}>Upcoming Appointment:</h3>
            <p>Patient: {profileData.upcomingAppointment.patient}</p>
            <p>Date: {profileData.upcomingAppointment.date}</p>
            <p>Time: {profileData.upcomingAppointment.time}</p>
            <p>Reason for Visit: {profileData.upcomingAppointment.reason}</p>
            <Link href="/login/doctor/doctorside/appointments" passHref>
              <button style={{color: "red"}}>Show All</button>
            </Link>
          </section>
          
          <section className={styles.card}>
            <h3 className={styles.boldTitle}>Last Consultation:</h3>
            <p>Patient: {profileData.lastConsultation.patient}</p>
            <p>Date: {profileData.lastConsultation.date}</p>
            <p>Time: {profileData.lastConsultation.time}</p>
            <p>Diagnosis: {profileData.lastConsultation.diagnosis}</p>
            <p>Treatment: {profileData.lastConsultation.treatment}</p>
            <Link href="/login/doctor/doctorside/history" passHref>
              <button style={{color: "red"}}>Show All</button>
            </Link>
          </section>
          
          <section className={styles.card}>
            <h3 className={styles.boldTitle}>Last Issued Prescription:</h3>
            <p>{profileData.lastIssuedPrescription.medication} to {profileData.lastIssuedPrescription.patient}</p>
            <Link href="/login/doctor/doctorside/profile/Prescriptions" passHref>
              <button style={{color: "red"}}>Show All</button>
            </Link>
          </section>
        </main>
      </div>

      <footer className={styles.footer}>
        <p>&copy; 2023 Hospital Portal. All rights reserved.</p>
      </footer>
    </>
  );
};

export default Page;