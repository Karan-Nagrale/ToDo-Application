# Django To-Do Application

A simple To-Do List web application built using Python and Django. This application helps users manage their daily tasks by adding, editing, deleting, and tracking completed and pending tasks.

## Features

- Add new tasks.
- View all tasks.
- Mark tasks as completed.
- Mark completed tasks as pending again.
- Edit existing tasks.
- Delete tasks.
- Store task information in an SQLite database.
- Manage tasks through the Django admin panel.

## Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite
- Git and GitHub

## Project Structure

```text
TODO/
│
├── env/
│
├── templates/
│   ├── edit_task.html
│   └── home.html
│
├── todo_main/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
│
├── todos/
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── db.sqlite3
├── manage.py
└── README.md
```

## Installation and Setup

Follow these steps to run this project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/Karan-Nagrale/ToDo-Application.git
```

### 2. Open the Project Folder

```bash
cd TODO
```

### 3. Create a Virtual Environment

```bash
python -m venv env
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\env\Scripts\activate
```

### 5. Install Django

```bash
pip install django
```

### 6. Apply Migrations

```bash
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

### 8. Open the Application

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## Learning Outcomes

Through this project, I learned:

- Django project and app structure.
- Creating Django models.
- Working with Django ORM.
- Performing CRUD operations.
- Handling GET and POST requests.
- Connecting HTML templates with Django views.
- Working with SQLite databases.
- Using Git and GitHub for version control.

## Author

**Karan Nagrale**

- GitHub: https://github.com/Karan-Nagrale
- LinkedIn: https://www.linkedin.com/in/karan-nagrale/