"use client";

import React, { useState, useEffect } from 'react';
import Navbar from '../../../../../components/navigation/navbar';
import styles from './DoctorsPage.module.css';

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

interface Doctor {
  firstName: string;
  lastName: string;
  qualification: string;
}

const doctor: Doctor = {
  firstName: 'John',
  lastName: 'Johnson',
  qualification: 'Cardiologist',
};

const Page = () => {
  const [currentDate, setCurrentDate] = useState(new Date());
  const [showPopup, setShowPopup] = useState(false);
  const [selectedAppointment, setSelectedAppointment] = useState<AppointmentDetails | null>(null);
  const [bookingDate, setBookingDate] = useState('');
  const [bookingTime, setBookingTime] = useState('');
  const [reasonForVisit, setReasonForVisit] = useState('');

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

  const handleBookAppointment = () => {
    console.log({
      doctorName: `${doctor.firstName} ${doctor.lastName}`,
      date: bookingDate,
      time: bookingTime,
      reason: reasonForVisit,
    });
    alert('Appointment booked successfully!');
    setBookingDate('');
    setBookingTime('');
    setReasonForVisit('');
  };

  return (
    <>
      <Navbar navbarType="client" />
      <div className={styles.doctorInfo}>
        <h1>{doctor.firstName} {doctor.lastName}</h1>
        <p>{doctor.qualification}</p>
      </div>
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
        <div className={styles.bookingForm}>
        <h2>Book an Appointment</h2>
        <input 
          type="date" 
          value={bookingDate} 
          onChange={(e) => setBookingDate(e.target.value)} 
        />
        <input 
          type="time" 
          value={bookingTime} 
          onChange={(e) => setBookingTime(e.target.value)} 
        />
        <textarea 
          placeholder="Reason for visit" 
          value={reasonForVisit} 
          onChange={(e) => setReasonForVisit(e.target.value)} 
        />
        <button onClick={handleBookAppointment}>Book Appointment</button>
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