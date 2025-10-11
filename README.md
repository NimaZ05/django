# 🌐 My Django Web Project: [Django-BLog]

## A Robust, Multi-App Web Application

This project is a modern web application built on the **Django framework**. It's structured to demonstrate key web development principles, including modular design, secure user management, and content creation.

It features a dedicated structure for **user authentication**, a **blogging system**, and **static content pages**.

---

## ✨ Key Features

* **[Complete User Account Management]** 
* **[Simple and Clean Post Editor]** 
* **[Responsive UI using CSS]**
* Secure user registration, login, and profile updating via the **`accounts`** app.
* Content management for articles and posts through the **`blog`** app.
* Uses a standard **MIT License**, making it easy for others to use and contribute.

---

## 🛠️ Get Started

Follow these steps to set up the project locally for development and testing.

### Prerequisites

You'll need:
* **Python 3.x**
* **pip** (Python package installer)

### Installation

1.  **Clone the Repository**

    ```bash
    git clone [https://github.com/NimaZ05/django.git](https://github.com/NimaZ05/django.git)
    cd django
    ```

2.  **Set up the Virtual Environment**

    We highly recommend using a virtual environment to isolate dependencies:

    ```bash
    # Create the environment
    python3 -m venv venv

    # Activate (macOS/Linux)
    source venv/bin/activate

    # Activate (Windows)
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies**

    Install all required packages listed in `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Database Migration**

    Apply the initial database schema to your local SQLite file:

    ```bash
    python manage.py migrate
    ```

5.  **Create a Superuser**

    Create an admin account to access the Django Administration interface:

    ```bash
    python manage.py createsuperuser
    ```

---

## 🚀 Running the App

Start the Django development server:

```bash
python manage.py runserver
