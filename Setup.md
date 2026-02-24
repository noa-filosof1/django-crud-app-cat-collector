# Django Project Setup Guide

## Step 1: Create New Repository

- Create a new repository on GitHub
- Clone the repository to your local machine
- Open the project folder in VS Code

## Step 2: Install Django and activate Virtual Environment

- Install Django  
  `pipenv install django`
- Activate Virtual Env  
  `pipenv shell`

## Step 3: Create Django Project

- Create project  
  `django-admin startproject projectname .`

  Example: `django-admin startproject library .`

- Review file explorer to see files are made
- Run server to confirm setup  
  `python3 manage.py runserver`

## Step 4: Database Setup

- Create database in a new terminal

`createdb <db_name>`
Example: `createdb library`

- Update database configuration in `settings.py`

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'library',
    }
}
```

- Run initial migrations  
  `python3 manage.py migrate`

## Step 5: Create Django App

- Create app  
  `django-admin startapp books`

- Add app to `INSTALLED_APPS` in `settings.py`

## Step 6: Update URLs

- Create `urls.py` inside the new app
- Include app URLs in project `urls.py`
- Add basic home view and route

## Step 7: Create Superuser

- Create admin user  
  `python3 manage.py createsuperuser`
- Login at `/admin`

---

## Step 8: Create Book Model

- Define `Book` model in `models.py`
- Add fields (title, author, etc.)
- Register model in `admin.py`

---

## Step 9: Migrations

- To check if migrations need to run
  `python3 manage.py makemigrations --check`

- Create migrations  
  `python3 manage.py makemigrations`
- Apply migrations  
  `python3 manage.py migrate`
- Migrations update the database schema based on model changes

---

## Step 10: Views

- Create Class based List View for books
- Create Class Based Detail View for individual book
- Connect views to URLs using `.as_view()`

---

## Step 11: Templates

- Create `templates` folder
- Create `base.html`
- Create `home.html`
- Create `books/book_list.html`
- Create `books/book_detail.html`
- Connect templates to views

---

## Step 12: Run and Test

- Run development server  
  `python3 manage.py runserver`
- Visit home page
- Test list and detail views
- Confirm data displays correctly

## If cloning a project setup from someone else

- Activate Virtual environment
- Run `pipenv install`
- Create your db with the same name as mentioned in settings
- Run migrations `python manage.py migrate` only
- Run server

## Documentation:

Built-in template tags and filters: https://docs.djangoproject.com/en/6.0/ref/templates/builtins/
