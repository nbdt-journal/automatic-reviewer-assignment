import Header from './Header'
import styles from '../styles/Home.module.css'
import { useEffect } from 'react';
import { useState } from 'react';
import Navbar from './Navbar'

export default function Home() {
  const [token, setToken] = useState("");
  useEffect(() => {
    const token = localStorage.getItem('token');
    setToken(token)
  }, []);

  return (
    <div className={styles.container}>
      <Navbar />
      <main className={styles.main}>
        <div className={styles.user}>
          {
            token &&
            <>
              <h1 className={styles.title}>Welcome</h1>
              <p style={{ marginBottom: '10px' }}> </p> <br />
            </>
          }
          {
            !token &&
            <>
              <p className={styles.title}>Please log in to continue</p>
              <img src="no-user.jpg" alt="" className={styles.avatar} />
            </>
          }
        </div>
      </main>
    </div>
  )
}