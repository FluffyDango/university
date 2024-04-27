"use client"
import React, { use, useState } from 'react';
import { useRouter } from 'next/navigation';
import Navbar from '../../components/navigation/navbar';
import styles from './doctor.module.css';
import { postData } from '@/app/database';
import Cookies from 'js-cookie';

type DoctorLogin = {
  success: boolean;
};

const Page: React.FC = () => {
  const router = useRouter();

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault(); // don't reload the page
    setIsLoading(true);
    const body = {
      username: username,
      password: password
    };
    const data: { success?: boolean, id?: number, message?: string } | null = await postData("/patients/login", body);
    if (data != null && data.success && data.id) {
        console.log('Login successful');
        Cookies.set('doctorId', data.id.toString());
        router.push('/login/doctor/doctorside');
    }
    else if (data != null && data.success && data.id) {
      setErrorMessage('Failed to get user id');
      console.log('Failed to get id');
    }
    else if (data != null && !data.success  && data.message) {
      setErrorMessage(data.message);
      console.log(data.message);
    }
    else {
      setErrorMessage('Something went wrong');
      console.log('Invalid login');
    }
    setIsLoading(false);
  };

  return (
    <>
      <Navbar navbarType="home" />
      <div className={styles.loginContainer}>
      <form className={styles.loginForm} onSubmit={handleSubmit}>
        {errorMessage && <p>{errorMessage}</p>}
        <h1 className={styles.title}>Log In as Doctor</h1>
        <input type="username" placeholder="Username" className={styles.loginInput} value={username} onChange={e => setUsername(e.target.value)} />
        <input type="password" placeholder="Password" className={styles.loginInput} value={password} onChange={e => setPassword(e.target.value)} />
        <button type="submit" className={styles.loginButton} disabled={isLoading}>
          {isLoading ? 'Loading...' : 'Log In'}
        </button>
      </form>
        <footer className={styles.footer}>
          <p>&copy; 2023 Hospital Portal. All rights reserved.</p>
        </footer>
      </div>
    </>
  );
};

export default Page;