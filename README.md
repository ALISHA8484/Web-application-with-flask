# Flask Note-Taking Web Application 📝

This project is a simple yet secure web application developed for a 4th-semester Computer Engineering course. It allows users to register, log in, and manage personal notes. The application emphasizes backend fundamentals, including robust user authentication, role-based access control, and security against common web vulnerabilities.

## ✨ Features

* **User Authentication**: Secure user registration, login, and logout functionality. Passwords are securely hashed using `pbkdf2:sha256`.
* **Session Management**: A "Remember Me" option that uses persistent cookies for an extended login session.
* **Automatic Logout**: If "Remember Me" is not selected, the user is logged out automatically after a short period of inactivity (implemented via short-lived cookies).
* **Role-Based Access Control (RBAC)**:
    * **Regular User**: Can create, view, and delete their own notes after logging in.
    * **Admin User**: Has access to a special Admin Panel to view a list of all registered users in the system.
* **Note Management**: A simple interface for authenticated users to add and delete text-based notes.
* **Brute-Force Protection**: The login route is rate-limited to **5 attempts per minute** per IP address, preventing automated password-guessing attacks. A custom error page is shown if the limit is exceeded.
* **Automatic Admin Setup**: An administrator account is automatically created with predefined credentials on the first run of the application, simplifying setup.

---

## 🛠️ Tech Stack

* **Backend**: Python with the Flask web framework.
* **Database**: SQLite via the Flask-SQLAlchemy ORM.
* **Authentication**: Flask-Login for user session management.
* **Security**: Werkzeug for password hashing and Flask-Limiter for rate-limiting.
* **Frontend**: HTML, Jinja2 templating, and Bootstrap 4 for styling.

---

## 🚀 Getting Started

Follow these instructions to get a local copy of the project up and running.

### Prerequisites

* Python 3.x
* pip (Python package installer)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone <your-repository-url>
    cd <repository-folder>
    ```

2.  **Create and activate a virtual environment (recommended):**
    * On macOS/Linux:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```
    * On Windows:
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install the required packages:**
    ```sh
    pip install Flask Flask-SQLAlchemy Flask-Login Flask-Limiter
    ```

---

## ▶️ Running the Application

1.  Execute the `main.py` file from the root directory:
    ```sh
    python main.py
    ```
2.  The script will automatically:
    * Create the SQLite database file (`website/database.db`) if it doesn't exist.
    * Create a default **admin** user if one is not already present.
    * Start the Flask development server.

3.  Open your web browser and navigate to `http://127.0.0.1:5000`.

---

## 📋 Usage

### Regular User

1.  Navigate to the `/sign-up` page to create a new account.
2.  Log in with your new credentials.
3.  On the home page, you can add new notes and delete existing ones.

### Admin User

1.  Navigate to the `/login` page.
2.  Use the default admin credentials to log in:
    * **Email**: `admin@example.com`
    * **Password**: `admin1234`
3.  Upon logging in, you will be redirected to the `/admin` panel, where you can see a table of all users registered in the database.

### Testing Brute-Force Protection

1.  Go to the `/login` page.
2.  Attempt to log in with an incorrect password more than 5 times within one minute.
3.  You will be redirected to a "Too Many Requests" error page and blocked from attempting to log in again until the minute has passed.

---
## 🖼️ Images

### Login page

### Sign up page

### User panel

### Admin panel

### Bruteforce protection





