"use client"

import React from 'react';
import { useEffect, useState } from 'react';
import Navbar from '../../../../components/navigation/navbar'
import styles from './doctors.module.css';
import { getData } from '@/app/database';

type DoctorData = {
  doc_name: string;
  doc_surname: string;
  level: string;
};

const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');

const Page = () => {


  const handleSearch = (event: React.ChangeEvent<HTMLInputElement>) => {
    const term = event.target.value;
    setSearchTerm(term);
    setFilteredDoctors(
      term ? alphabetizedDoctors.filter(
        doctor => doctor.doc_name.toLowerCase().includes(term.toLowerCase()) ||
                  doctor.doc_surname.toLowerCase().includes(term.toLowerCase()) ||
                  doctor.level.toLowerCase().includes(term.toLowerCase())
      ) : alphabetizedDoctors
    );
  };

  const redirectToDoctorPage = (doctorLastName: any) => {
    window.location.href = `/login/client/clientside/doctors/DoctorsPage`;
  };

  const [doctorData, setDoctorData] = useState<DoctorData[]>([]);

  const alphabetizedDoctors = doctorData.sort((a, b) =>
    a.doc_surname.localeCompare(b.doc_surname)
  );

  const [searchTerm, setSearchTerm] = useState('');
  const [filteredDoctors, setFilteredDoctors] = useState(alphabetizedDoctors);

  useEffect(() => {
    const fetchData = async () => {
      const data: DoctorData[] = await getData('/doctors');
      if (data) {
        setDoctorData(data);
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
      <div className={styles.container}>
        <div className={styles.searchContainer}>
          <input
            type="text"
            placeholder="Search for a doctor..."
            value={searchTerm}
            onChange={handleSearch}
            className={styles.searchInput}
          />
        </div>
        {alphabet.map(letter => {
          const doctorsForLetter = filteredDoctors.filter(doctor => doctor.doc_surname.startsWith(letter));
          return doctorsForLetter.length > 0 && (
            <div key={letter} className={styles.letterSection}>
              <h2 className={styles.letterHeader}>{letter}</h2>
              {doctorsForLetter.map((doctor, index) => (
                <div key={index} 
                     className={styles.doctorCard} 
                     onClick={() => redirectToDoctorPage(doctor.doc_surname)}>
                  <div className={styles.doctorInfo}>
                    <h3>{doctor.doc_name} {doctor.doc_surname}</h3>
                    <p>{doctor.level}</p>
                  </div>
                </div>
              ))}
            </div>
          );
        })}
      </div>
    </>
  );
};

export default Page;