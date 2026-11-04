# To-Do List Web Application (Django)

A beginner-friendly, minimalist, and responsive To-Do List web application built using **Django**, **HTML**, and **CSS**.

---

## 📋 Features

- **Home Page (`/`)**: Displays all tasks in a structured, clean table with task counts (Total, Done, Pending).
- **Add Task (`/add/`)**: Simple form with `Title` and `Description` to create new tasks.
- **Update Task (`/edit/<id>/`)**: Edit an existing task's title, description, or completion status.
- **Toggle Status (`/toggle/<id>/`)**: One-click completion status toggle directly from the list table.
- **Delete Task (`/delete/<id>/`)**: Safe deletion workflow with confirmation prompt.
- **Status Distinction**: Completed tasks feature distinct visual cues (subtle strikethrough, muted tone, green checkmark).
- **Empty State**: Friendly "No tasks yet" message with a quick button when no tasks are present.
- **Security**: Built-in CSRF protection on all forms.
- **Django Admin Integration**: Manage tasks via Django's built-in administration panel.

---

## 🛠️ Project Structure

```text
to-do-list-webdev/
├── db.sqlite3                 # SQLite database
├── manage.py                  # Django management script
├── todoproject/               # Project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py            # Settings (installed apps, database, static files)
│   ├── urls.py                # Main URL router
│   └── wsgi.py
├── tasks/                     # To-Do application
│   ├── admin.py               # Django Admin model registration
│   ├── apps.py                # App configuration
│   ├── forms.py               # Task forms (TaskCreateForm, TaskUpdateForm)
│   ├── migrations/            # Database migrations
│   │   └── 0001_initial.py
│   ├── models.py              # Task model definition
│   ├── static/
│   │   └── css/
│   │       └── style.css      # Minimalist styling
│   ├── templates/
│   │   └── tasks/
│   │       ├── base.html              # Base layout with navbar and footer
│   │       ├── task_list.html         # Main dashboard and task table
│   │       ├── task_form.html         # Add and Edit task forms
│   │       └── task_confirm_delete.html # Delete confirmation
│   ├── tests.py               # Automated test suite
│   ├── urls.py                # App URL routing
│   └── views.py               # CRUD views & business logic
└── README.md
```

---

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have Python 3 and Django installed:

```bash
python3 -m pip install django
```

### 2. Apply Database Migrations

```bash
python3 manage.py migrate
```

### 3. (Optional) Seed Funny & Interesting Tasks

Populate your database with humorous sample tasks:

```bash
python3 manage.py seed_tasks
```

### 4. (Optional) Create an Admin Superuser

```bash
python3 manage.py createsuperuser
```

### 5. Run the Development Server

```bash
python3 manage.py runserver
```

Open your browser and navigate to:
**[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🧪 Running Automated Tests

Run the full suite of unit and integration tests:

```bash
python3 manage.py test
```

