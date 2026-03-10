# Job Application Tracker (Django)

## Overview

The **Job Application Tracker** is a web application built using **Django** that helps users manage and track their job applications efficiently. It allows users to store job details, track application status, and organize job search activities in one place.

## Features

* Add new job applications
* Update application status (Applied, Interview, Offer, Rejected)
* View all job applications in a structured table
* Search and filter job applications
* Edit and delete job records
* User-friendly interface

## Technologies Used

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, JavaScript
* **Database:** SQLite / MySQL
* **Tools:** Git, GitHub

## Project Structure

```
job_tracker/
│
├── jobs/                # Django app for job management
├── templates/           # HTML templates
├── static/              # CSS and JavaScript files
├── db.sqlite3           # Database file
├── manage.py
└── README.md
```

## Installation

### 1. Clone the repository

```
git clone https://github.com/lohith-2000/jobs_repo.git
```

### 2. Navigate to project directory

```
cd jobtracker
```

### 3. Create virtual environment (optional but recommended)

```
python -m venv venv
```

### 4. Activate virtual environment

**Windows**

```
venv\Scripts\activate
```

**Linux/Mac**

```
source venv/bin/activate
```

### 5. Install dependencies

```
pip install django
```

### 6. Apply migrations

```
python manage.py migrate
```

### 7. Run the development server

```
python manage.py runserver
```

Open the browser and go to:

```
http://127.0.0.1:8000/
```

## Future Improvements

* User authentication and login system
* Email notifications for interview reminders
* Dashboard analytics for job applications
* Integration with external job APIs

## Author

**Lohith**

---

⭐ If you like this project, feel free to star the repository.
