# StraySafe

IT course Semester 4. Problem-based project. 15 Credits (Half of the semester credits)
This is still the unfinished version, because the semester has not come to an end yet

#### Team members

 - Gerdvila Edvinas
 - Narbutas Renaldas
 - Nikulin Arsenij

## Project topic: *Lost animals platform*

#### Task description

Develop an web app /web platform that lets you tag a location of where you found a lost animal. With this kind of app you could potentially share the picture, location, comments, etc. with someone who has lost an animal so that they could find it. As an addition having the location of the nearest clinic or shelter nearby could make it even easier to take them some place safe. The system must integrate smart solutions and include several algorithms to support big amounts of users around the world.

#### Vision

TODO

## Overview
 - Frontend framework: Angular
 - Backend framework: Spring Boot Java
 - Database: PostgreSql
 - Project setup tool: Ansible, npm


# Server Setup

There are ansible scripts made to setup the whole system in `ansible` folder.

## [Debian] Developers setup

#### Dependencies
TODO
```bash
sudo apt install npm
sudo npm install -g @angular/cli
```

Install nvm using (This is v0.39.7, you can find latest [here](https://nvm.sh)):
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```
Install 20.11.0 node LTS (Long Term Support) version which works with angular
```bash
nvm install 20.11.0
```

#### Database setup
Install latest version:
```bash
sudo apt install postgresql -y
```

Setup postgres user password
```bash
sudo -u postgres psql
```
```bash
ALTER USER postgres WITH PASSWORD 'newpassword';
CREATE DATABASE straysafe;
```
Launch sql files located in `./ansible/sql`
```bash
psql -U postgres -d straysafe -f "file_one.sql"
```

Open the file pg_hba.conf.
```bash
sudo nano /etc/postgresql/<your_psql_version>/main/pg_hba.conf
```
First line of the settings should be. This will make it that only all IP and all users will be able to connect.
```bash
local all all md5
```

Restart the postgresql server:
```bash
sudo systemd restart postgresql
```

Don't forget to setup a .env file at:`./src/backend/src/main/resources`. Example:
```
DATABASE_IP=111.111.111.111
DB_PORT=2024
DB_NAME=straysafe
DB_USERNAME=postgres
DB_PASSWORD=newpassword
```

## [Windows] Developers setup

#### Dependencies

Download and run nvm setup [here](https://github.com/coreybutler/nvm-windows/releases)

Install 20.11.0 node LTS (Long Term Support) version which works with angular. This will download npm as well.
```bash
nvm install 20.11.0
```
Install angular CLI (This is global installation, not sure if it would work like this)
```bash
npm install -g @angular/cli
```

## Launch website
TODO
