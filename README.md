# Taskify

Taskify is a simple task management application built with Django. It allows users to create, edit, delete, and manage tasks. Users can also add comments to tasks and dynamically add new categories.

## Features

- User authentication (login, logout, register)
- Create, edit, delete tasks
- Mark tasks as complete/incomplete
- Add comments to tasks

## Design

A simple interface design with light and dark mode:

![Screenshot 2025-02-03 150935](https://github.com/user-attachments/assets/2a8ea86d-8393-4645-b58b-58d580cfda8d)

![Task](https://github.com/user-attachments/assets/8542366e-e50d-4706-87a0-4e41ce9afe71)

Colour pallette:

![colours](https://github.com/user-attachments/assets/86053ca2-6b98-400b-be3b-9a4d986e691a)

## Responsive Design:

![responsive](https://github.com/user-attachments/assets/7340aa10-3d46-4917-b64c-7de753fd124a)



## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/taskify.git
    cd taskify
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the environment variables:
    ```sh
    cp .env.example .env
    ```

5. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

6. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

7. Run the development server:
    ```sh
    python manage.py runserver
    ```

8. Open your browser and go to `http://localhost:8000`.

## Usage

- Register a new account or log in with an existing account.
- Create a new task by clicking on the "New Task" button.
- Edit or delete tasks by clicking on the respective buttons in the task detail view.
- Mark tasks as complete or incomplete by clicking on the "Mark as Complete/Incomplete" button.
- Add comments to tasks in the task detail view.

## Deployment

To deploy this application to Heroku, follow these steps:

1. Log in to Heroku:
    ```sh
    heroku login
    ```

2. Create a new Heroku app:
    ```sh
    heroku create
    ```

3. Set up the environment variables on Heroku:
    ```sh
    heroku config:set SECRET_KEY=your_secret_key
    heroku config:set DATABASE_URL=your_database_url
    ```

4. Push the code to Heroku:
    ```sh
    git push heroku main
    ```

5. Apply the migrations on Heroku:
    ```sh
    heroku run python manage.py migrate
    ```

6. Create a superuser on Heroku:
    ```sh
    heroku run python manage.py createsuperuser
    ```

7. Open your Heroku app in the browser:
    ```sh
    heroku open
    ```
