
# Flask CRUD Operation

This project is a simple Flask web application that demonstrates basic CRUD (Create, Read, Update, Delete) operations using Flask and SQLAlchemy with a SQLite database. The app allows you to manage a list of users with a username and name.

## Features

- Add new users
- List all users
- Update user information
- Delete users
- Simple, clean UI with HTML and CSS

## Project Structure

```
├── app.py                # Main Flask application
├── instance/
│   └── site.db           # SQLite database file
├── static/
│   ├── index.css         # CSS for home page
│   ├── user_form.css     # CSS for user forms
│   └── users_list.css    # CSS for users list
├── Templates/
│   ├── index.html        # Home page
│   ├── user_form.html    # Add user form
│   ├── update_user.html  # Update user form
│   └── users.html        # List users
├── README.md
└── LICENSE
```

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Flask-SQLAlchemy

You can install the required packages using pip:

```bash
pip install flask flask_sqlalchemy
```

### Running the Application

1. Make sure you are in the project directory.
2. Run the Flask app:

```bash
python app.py
```

3. Open your browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Application Routes

- `/` : Home page
- `/users` : List all users
- `/user-form` : Add a new user
- `/add_user` : POST endpoint to add user
- `/update-user/form-<id>` : Show update form for user
- `/update-user` : POST endpoint to update user
- `/delete-user-<id>` : Delete a user

## Database

The app uses SQLite (file: `instance/site.db`) via SQLAlchemy ORM. The `User` model has the following fields:

- `id` (Integer, Primary Key)
- `username` (String, Unique, Required)
- `name` (String, Unique, Required)

## Screenshots

_Add screenshots of the UI here if desired._

## License

This project is licensed under the terms of the MIT License.
