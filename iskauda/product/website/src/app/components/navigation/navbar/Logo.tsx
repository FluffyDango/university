"use client";
import Image from "next/image";
import { useEffect, useState } from "react";
import Button from "./SignUpButton";
import styles from './logo.module.css';

const Logo = () => {
  
  const [width, setWidth] = useState(0);

  const updateWidth = () => {
    const newWidth = window.innerWidth;
    setWidth(newWidth);
  };

  useEffect(() => {
    window.addEventListener("resize", updateWidth);
    updateWidth();
  }, []);

  const [showButton, setShowButton] = useState(false);

  const changeNavButton = () => {
    if (window.scrollY >= 400 && window.innerWidth < 768) {
      setShowButton(true);
    } else {
      setShowButton(false);
    }
  };

  useEffect(() => {
    window.addEventListener("scroll", changeNavButton);
  }, []);

  return (
    <>
      {showButton ? (
        <Button />
      ) : (
          <div className={styles.logoWrapper}>
            <Image
              src="/images/1.png"
              alt="Logo"
              width={150}
              height={45}
              style={{ width: 'auto', height: '200%' }}
            />
          </div>
      )}
    </>
  );
};

export default Logo;