"use client";
import React from 'react';
import { useEffect, useState } from 'react';
import Navbar from '../../../../components/navigation/navbar';
import styles from './appointments.module.css';
import { getData } from '@/app/database';
import Cookies from 'js-cookie';

type Appointment = {
  doc_name: string;
  doc_surname: string;
  level: string;
  start_time: string;
  slot_date: string;
};

const Page: React.FC = () => {
  const [appointmentsData, setAppointmentsData] = useState<Appointment[]>([]);

  useEffect(() => {
    const fetchData = async () => {
      const data: Appointment[] = await getData('/appointment/' + Cookies.get('patientId'));
      if (data) {
        setAppointmentsData(data);
      } else {
        console.log('Something went wrong');
        console.log(data);
      }
    };
    fetchData();
  }, []);

  return (
    <>
      <Navbar navbarType="client" />
      <div className={styles.appointmentsContainer}>
        <h1 className={styles.title}>Future Appointments:</h1>
        {appointmentsData.map((appointment, index) => (
          <div key={index} className={styles.card}>
            <h3 className={styles.boldTitle}>Future Appointment:</h3>
            <p>Doctor: {appointment.doc_name} {appointment.doc_surname}</p>
            <p>Level: {appointment.level}</p>
            <p>Date: {appointment.slot_date}</p>
            <p>Time: {appointment.start_time}</p>
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