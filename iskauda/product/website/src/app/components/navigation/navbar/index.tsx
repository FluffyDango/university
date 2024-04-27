import React from "react";
import Link from "next/link";
import Logo from "./Logo";
import { SignUpButton } from "./SignUpButton";
import { LogInButton } from "./LogInButton";
import { LogOutButton } from "./LogOutButton";

interface NavbarProps {
  navbarType: "home" | "client" | "doctor";
}

const Navbar: React.FC<NavbarProps> = ({ navbarType }) => {
  return (
    <nav className="w-full h-20 bg-red-800 sticky top-0 z-50">
      <div className="container mx-auto px-4 h-full">
        <div className="flex justify-between items-center h-full">
        
          {navbarType === "client" ? (
            <Link href="/login/client/clientside"><Logo /></Link>
          ) : navbarType === "doctor" ? (
            <Link href="/login/doctor/doctorside"><Logo /></Link>
          ) : (
            <Link href="/"><Logo /></Link>
          )}

          {navbarType === "home" ? (
            <div className="flex items-center md:order-2">
              <Link href="/login"><LogInButton /></Link>
              <Link href="/signup"><SignUpButton /></Link>
            </div>
          ) : navbarType === "client" ? (
            <>
              <div className="hidden md:flex justify-center flex-grow items-center">
                <ul className="flex gap-x-6 text-white items-center">
                  <li><Link href="/login/client/clientside">Home</Link></li>
                  <li><Link href="/login/client/clientside/doctors">Doctors</Link></li>
                  <li><Link href="/login/client/clientside/appointments">Appointments</Link></li>
                  <li><Link href="/login/client/clientside/history">History</Link></li>
                  <li><Link href="/login/client/clientside/profile">Profile</Link></li>
                  <li><Link href="/login/client/clientside/calendar">Calendar</Link></li>
                </ul>
              </div>
              <div className="flex items-center md:order-3">
                <Link href="/"><LogOutButton /></Link>
              </div>
            </>
          ) : navbarType === "doctor" ? (
            <>
              <div className="hidden md:flex justify-center flex-grow items-center">
                <ul className="flex gap-x-6 text-white items-center">
                  <li><Link href="/login/doctor/doctorside">Home</Link></li>
                  <li><Link href="/login/doctor/doctorside/appointments">Appointments</Link></li>
                  <li><Link href="/login/doctor/doctorside/history">History</Link></li>
                  <li><Link href="/login/doctor/doctorside/profile">Profile</Link></li>
                  <li><Link href="/login/doctor/doctorside/calendar">Calendar</Link></li>
                </ul>
              </div>
              <div className="flex items-center md:order-3">
                <Link href="/"><LogOutButton /></Link>
              </div>
            </>
          ) : null }
        </div>
      </div>
    </nav>
  );
};

export default Navbar;