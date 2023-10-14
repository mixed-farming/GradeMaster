Django-Simple-CRUD-Sample

## Description

GradeMaster is an innovative and user-friendly web-based platform designed to improve communication between teachers and parents. It allows teachers to input and update student academic data, attendance, and remarks, while parents can view their child's progress in real-time and receive notifications about their academic performance. The platform has been designed using the Django web framework, HTML, CSS, JavaScript, and Bootstrap, which ensures a user-friendly interface for all users. The project also incorporates features to ensure data security and confidentiality, such as using SQLite as the database management system and the FullCalendar content delivery network to facilitate the marking of student attendance records.

## Version

Django 2.0.2

## Usage

Windows Command Prompt

```
cd Django-Simple-CRUD-Sample
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
manage.py migrate
manage.py createsuperuser 
manage.py runserver
```

Open URL http://localhost:8000
