import React from 'react';
import Link from 'next/link';
import Navbar from '../components/navigation/navbar';
import styles from './login.module.css';

const page: React.FC = () => {
  return (
    <>
      <Navbar navbarType="home" />
    <div className={styles.loginContainer}>
      <div className={styles.header}>
      </div>
      <div className={styles.mainContent}>
        <div className={styles.buttonContainer}>
        <Link href="/login/doctor" passHref>
            <button className={styles.loginButton}>Log In as Doctor</button>
          </Link>
          <Link href="/login/client" passHref>
            <button className={styles.loginButton}>Log In as Client</button>
          </Link>
        </div>
      </div>
      <footer className={styles.footer}>
        <p>&copy; 2023 Hospital Portal. All rights reserved.</p>
      </footer>
      </div>
      </>
  );
};

export default page;
