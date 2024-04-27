"use client";

import React from 'react';
import { useEffect, useState } from 'react';
import Navbar from '../../../../components/navigation/navbar';
import styles from './calendar.module.css';
import { getData } from '@/app/database';
import Cookies from 'js-cookie';

interface DayData {
  dayNum: number;
  isToday: boolean;
  hasAppointment: boolean;
}

interface AppointmentDetails {
  doctorName: string;
  qualification: string;
  date: string;
  time: string;
  notes: string;
}

// SELECT doc_name, doc_surname, level, slot_date, start_time, end_time FROM doctor, timeslot
// WHERE doc_id_slot = doc_id;

const appointments = [
  {
    doctorName: 'Dr. Peter Peterson',
    qualification: 'Cardiologist',
    date: '2024-04-20',
    time: '10:00',
    notes: 'Future Appointment',
  },
  {
    doctorName: 'Dr. Bob Boobson',
    qualification: 'Urologist',
    date: '2023-12-29',
    time: '11:00',
    notes: 'Future Appointment',
  },
  {
    doctorName: 'Dr. John Borsch',
    qualification: 'General Practitioner',
    date: '2023-01-20',
    time: '09:00',
    notes: 'Body weight is above recommended.',
  },
  {
    doctorName: 'Dr. Hannah Robbins',
    qualification: 'Dentist',
    date: '2022-12-15',
    time: '15:00',
    notes: 'No issues found.',
  },
  {
    doctorName: 'Dr. Jordan Jordanson',
    qualification: 'Cardiologist',
    date: '2022-11-10',
    time: '14:00',
    notes: 'Annual blood work. All results within normal ranges.',
  }
];

const today = new Date();

const Page = () => {
  const [currentDate, setCurrentDate] = useState(new Date());
  const [showPopup, setShowPopup] = useState(false);
  const [selectedAppointment, setSelectedAppointment] = useState<AppointmentDetails | null>(null);

  const daysInMonth = (month: number, year: number) => new Date(year, month + 1, 0).getDate();

  const getMonthDays = (month: number, year: number): DayData[] => {
    let days: DayData[] = [];
    for (let i = 1; i <= daysInMonth(month, year); i++) {
      const dayDate = new Date(year, month, i);
      days.push({
        dayNum: i,
        isToday: dayDate.toDateString() === today.toDateString(),
        hasAppointment: appointments.some(app => new Date(app.date).toDateString() === dayDate.toDateString()),
      });
    }
    return days;
  };  

  const handleDayClick = (day: DayData) => {
    const appointmentForDay = appointments.find(app => new Date(app.date).getDate() === day.dayNum && new Date(app.date).getMonth() === currentDate.getMonth() && new Date(app.date).getFullYear() === currentDate.getFullYear());
    if (appointmentForDay) {
      setSelectedAppointment(appointmentForDay);
      setShowPopup(true);
    }
  };

  const closePopup = () => setShowPopup(false);

  const prevMonth = () => setCurrentDate(new Date(currentDate.getFullYear(), currentDate.getMonth() - 1, 1));
  const nextMonth = () => setCurrentDate(new Date(currentDate.getFullYear(), currentDate.getMonth() + 1, 1));

  const monthDays = getMonthDays(currentDate.getMonth(), currentDate.getFullYear());

  return (
    <>
      <Navbar navbarType="client" />
      <div className={styles.calendarContainer}>
        <div className={styles.header}>
          <button onClick={prevMonth}>&lt;</button>
          <h1>{currentDate.toLocaleString('default', { month: 'long' })} {currentDate.getFullYear()}</h1>
          <button onClick={nextMonth}>&gt;</button>
        </div>
        <div className={styles.calendarGrid}>
          {monthDays.map((day: DayData) => (
            <div 
              key={day.dayNum} 
              className={`${styles.day} ${day.isToday ? styles.today : ''} ${day.hasAppointment ? styles.appointment : ''}`} 
              onClick={() => handleDayClick(day)}
            >
              {day.dayNum}
            </div>
          ))}
        </div>
        {showPopup && selectedAppointment && (
          <div className={styles.popup}>
            <button onClick={closePopup} className={styles.closeBtn}>X</button>
            <p><strong>Doctor:</strong> {selectedAppointment.doctorName}</p>
            <p><strong>Qualification:</strong> {selectedAppointment.qualification}</p>
            <p><strong>Date:</strong> {selectedAppointment.date}</p>
            <p><strong>Time:</strong> {selectedAppointment.time}</p>
            <p><strong>Notes:</strong> {selectedAppointment.notes}</p>
          </div>
        )}
      </div>
      <footer className={styles.footer}>
        <p>&copy; 2023 Hospital Portal. All rights reserved.</p>
      </footer>
    </>
  );
};

export default Page;