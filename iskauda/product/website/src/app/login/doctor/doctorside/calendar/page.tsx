"use client";

import React, { useState, useEffect } from 'react';
import Navbar from '../../../../components/navigation/navbar';
import styles from './calendar.module.css';

interface DayData {
  dayNum: number;
  isToday: boolean;
  hasAppointment: boolean;
}

interface AppointmentDetails {
  patientName: string;
  date: string;
  time: string;
  reason: string;
}

const appointments = [
  {
    patientName: 'Peter Peterson',
    date: '2024-04-20',
    time: '10:00',
    reason: 'Check-up',
  },
  {
    patientName: 'Jordan Jordanson',
    date: '2023-12-29',
    time: '14:00',
    reason: 'Follow-up for bloodwork',
  },
  {
    patientName: 'Jeff Jeffer',
    date: '2023-01-20',
    time: '09:30',
    reason: 'High blood pressure treatment',
  },
  {
    patientName: 'Olaf Olafson',
    date: '2022-12-15',
    time: '13:00',
    reason: 'Routine Dental Check-up',
  },
  {
    patientName: 'Richard Richardson',
    date: '2022-11-10',
    time: '15:00',
    reason: 'Annual Blood Work',
  }
];

const today = new Date();

const Page = () => {
  const [currentDate, setCurrentDate] = useState(new Date());
  const [showPopup, setShowPopup] = useState(false);
  const [selectedAppointment, setSelectedAppointment] = useState<AppointmentDetails | null>(null);

  useEffect(() => {
    setSelectedAppointment(null);
    setShowPopup(false);
  }, [currentDate]);

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
      <Navbar navbarType="doctor" />
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
            <p><strong>Patient:</strong> {selectedAppointment.patientName}</p>
            <p><strong>Date:</strong> {selectedAppointment.date}</p>
            <p><strong>Time:</strong> {selectedAppointment.time}</p>
            <p><strong>Reason for Visit:</strong> {selectedAppointment.reason}</p>
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