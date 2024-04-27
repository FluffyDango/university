"use client"
import React, { useState } from 'react';
import { useRouter } from 'next/navigation'
import Navbar from '../components/navigation/navbar';
import styles from './signup.module.css';
import { postData } from '@/app/database';

const Page: React.FC = () => {
  const router = useRouter();

  const [name, setName] = useState('');
  const [surname, setSurname] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault(); // don't reload the page
    setIsLoading(true);
    const body = {
      name: name,
      surname: surname,
      username: username,
      password: password
    };
    const data: { success?: boolean, message?: string } | null = await postData("/patients", body);
    if (data != null && data.success) {
        console.log('Signup successful');
        router.push('/login/client/clientside');
    }
    else if (data != null && !data.success && data.message) {
      setErrorMessage(data.message);
      console.log(data.message);
    }
    else {
      console.log('Error signing up');
    }
    setIsLoading(false);
  };
  return (
    <>
      <Navbar navbarType="home" />
     <div className={styles.signUpContainer}>
      <form className={styles.signUpForm} onSubmit={handleSubmit}>
      {errorMessage && <p>{errorMessage}</p>}
      <h1 className={styles.title}>Sign Up</h1>
        <input type="text" placeholder="First Name" value={name} onChange={e => setName(e.target.value)} required />
        <input type="text" placeholder="Last Name" value={surname} onChange={e => setSurname(e.target.value)} required />
        <input type="username" placeholder="Username" value={username} onChange={e => setUsername(e.target.value)} required />
        <input type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} required />
        <button type="submit" disabled={isLoading}>
          {isLoading ? 'Loading...' : 'Sign Up'}
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