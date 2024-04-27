import React from 'react';
import Navbar from '../../../components/navigation/navbar'
import styles from './home.module.css';

const page: React.FC = () => {
  return (
    <>
      <Navbar navbarType="client" />
    <div className={styles.homeContainer}>
      <div className={styles.header}>
        <h1 className={styles.boldTitle}>Welcome to Our Hospital</h1>
        <p>Working since 1964</p>
      </div>

      <main className={styles.mainContent}>
        <section className={styles.stats}>
          <h2 className={styles.boldTitle}>ABOUT US:</h2>
          <p>Over 50,000 surgeries performed</p>
          <p>More than 200,000 patient visits each year</p>
          <p>Home to 300 dedicated doctors</p>
          <p>Witness to over 1,000 newborns every year</p>
        </section>

        <section className={styles.awards}>
        <h2 className={styles.boldTitle}>AWARDS:</h2>
          <ul>
            <li>2010 Hospital of the Year</li>
            <li>2015 Top 15 hospital in European Union</li>
          </ul>
        </section>

        <section className={styles.faq}>
        <h2 className={styles.boldTitle}>FAQ:</h2>
          <div className={styles.faqItem}>
            <p>Question 1</p>
            <p>Answer 1.</p>
          </div>
          <div className={styles.faqItem}>
            <p>Question 2</p>
            <p>Answer 2.</p>
          </div>
        </section>

        <section className={styles.contactInfo}>
        <h2 className={styles.boldTitle}>Contact Information:</h2>
          <p>Phone: +1234567890</p>
          <p>Working Days/Hours: Mon-Sun / 9:00 AM - 8:00 PM</p>
          <p>Email: contact@vbhospital.com</p>
        </section>
      </main>

      <footer className={styles.footer}>
        <p>&copy; 2023 Hospital Portal. All rights reserved.</p>
      </footer>
    </div>
    </>
  );
};

export default page;