# pullOut Team

IT Course semester 3 problem-based project. The subject was worth 15 credits, that is half of the semester credits + 5 credits which were combined from Programming software subject. In total 20 credits.

## Team members:
 - *Morozov Oleksii*
 - *Namajūnas Joris*
 - *Narbutas Renaldas*
 - *Stankevič Severyn*

## Project topic: *Digitalization of a business card*

#### Short description: 

*Paper contact card conversion to a digital format.*

#### Vision:

Using this application, user should be able to provide images which would be analyzed to digital versions
of contact information, called vCards. The program can be used locally, but it can be synced with a CardDav server
as well. User is able to export all of this information to PDF or ICS formats, or send the data to a new
CardDav server of his liking.

## Overview
 - Programming language: Python
 - User local database: SQLite
 - CardDav server database: PostgreSQL
 - Image to text OCR: Tesseract
 - Image filtering: OpenCV
 - Named entity recognition: Spacy
 - Testing: UnitTest
 - Build tool: Poetry
 - System setup tool: Ansible


# Setup

### Ansible system setup

There are ansible scripts made to setup the whole system in `ansible` folder.

### [Debian] Client setup without ansible

If you only need to download client and cannot use the ansible scripts, use the below instructions

Download pip, tesseract and the Lithuanian + English tesseract language models 
```bash
sudo apt install pip python3-opencv tesseract-ocr-lit
```
Download pullout CLI
```bash
pip install src/client
```

### [Windows] Client setup without ansible
- Python can be found in Microsoft store
- Pip can be installed using this [guide](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/)
- Tesseract in Windows there is no official installation for newer versions. Choices are:
  - Mannheim University Library installation script which can be found [here](https://github.com/UB-Mannheim/tesseract/wiki)
  - [Cygwin](https://cygwin.com/cgi-bin2/package-grep.cgi?grep=tesseract&arch=x86_64) installation
  - Compile from [source code](https://github.com/tesseract-ocr/tesseract)
  - Use Windows subsystem linux (WSL) and dowload everything using linux install commands
  - For more information check the [Tesseract documetation page](https://tesseract-ocr.github.io/tessdoc/Installation.html)
  - Don't forget to download ENG and LIT models of tesseract
- Last step is to install the application:
```
pip install src/client
```

### [Debian] Database setup
1. Install dependencies:
```bash
sudo apt install postgresql-contrib python3-psycopg2 apache2 php php-curl php-xml php-pgsql libapache2-mod-php
```
2. Get composer setup:
```bash
curl -sS https://getcomposer.org/installer -o composer-setup.php
HASH=`curl -sS https://composer.github.io/installer.sig`
```
3. Run installer:
```bash
php -r "sudo php composer-setup.php --install-dir=/usr/local/bin --filename=composer"
```
4. Setup apache server and put server.php wtih composer files in apache server folder.
5. Run composer install
6. Configure Postgresql and create .env in apache server folder with credentials, example:
```
DB_HOST=localhost
DB_NAME=test
DB_USER=test
DB_PASSWORD=1251
```
7. Run all sql files in `src/database/src/sql/*.sql`

### [DEVELOPERS] Poetry build tool
Linux, MacOS:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Windows (powershell)
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

### [DEVELOPERS] Getting python dependencies
In order for vscode to recognize packages, build dependencies in project folder `.venv`. To do this, type:
```bash
poetry config virtualenvs.in-project true
```
Go to the server folder and type
```bash
poetry install
```
It will make a virtual environment for that specific server and download dependencies

Install PoeThePoet for quick commands to run
```bash
pip install poethepoet
```

### Run code example
```bash
poetry shell
pullout --help
```

Test with PoeThePoet
```bash
poe test
```

NOTE: You have to be in the specific directory, else it will not understand which `pyproject.toml` you are asking poetry to run.


### Example photos
A few can be found in `src/client/assets/photos`. More with which the program was tested on, can be found in this [google drive link](https://drive.google.com/drive/folders/1RMf1kKzsd8fB02sFniFgrXqjq3WZevqn?usp=drive_link)