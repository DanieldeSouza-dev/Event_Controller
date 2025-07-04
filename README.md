
# 🖥️🐍 Event Control System based in Python

![Status](https://img.shields.io/badge/status-complete-blue)
![Built with](https://img.shields.io/badge/built%20with-Python%203.13-yellow)

This is an object-oriented event management system built in Python, featuring JSON-based persistence. It supports staff and user registration, show management, and allows users to browse and save favorite shows.


## 📦 Project Structure

```
📂 Event_Controller/
│
├── .gitignore              # Files/folders excluded from version control
├── src/                    # Source code directory
│   ├── core/               # Core logic: authentication, persistence, validators, system control
│   │   ├── authentication.py
│   │   ├── persistence.py            
│   │   ├── system.py                 
│   │   ├── validators.py
│   │   └── menu_functions/           # Logic behind staff/user menu options
│   │       ├── staff_menu_functions.py
│   │       └── user_menu_functions.py
│   ├── data/               # JSON-based persistence for users, staff, shows, and favorites
│   │   ├── staff.json 
│   │   ├── users.json
│   │   ├── shows.json
│   │   └── favorites/              # Individual JSON files for user favorites
│   ├── interface/          # CLI interface and user navigation
│   │   └── menu.py                 
│   ├── models/             # Core class definitions: Person, User, Staff, Show
│   │   ├── person.py               
│   │   ├── user.py                 
│   │   ├── staff.py                
│   │   └── shows.py                
│   └── tests/              # Unit tests for each module
│       ├── test_person.py
│       ├── test_user.py
│       ├── test_staff.py
│       ├── test_shows.py
│       ├── test_authentication.py
│       ├── test_system.py
│       └── test_menu.py
│
└── main.py  # Entry point for running the system
```

## 🧩 Implemented Features

### Main
- Acts as the main entry point of the system. Starts the application and connects the interface with core functionalities. Initializes data, handles program flow, and delegates control to the CLI interface.

### Core/
- Contains the system’s core logic, including:

    - `authentication.py:` Manages user and staff login via ID and password.

    - `system.py:` Controls high-level logic and routing for staff/user operations.

    - `persistence.py:` Handles all JSON-based data storage and retrieval.

    - `validators.py:` Validates fields like CPF, names, and passwords.

    - `menu_functions/:` Splits functions into `staff_menu_functions.py` and `user_menu_functions.py` for better separation of responsibilities.

### Data/
- Stores persistent data in JSON format.
Includes:

    - `staff.json`, `users.json`, and `shows.json` for system data.

    - A `favorites/` folder where each user's favorite shows are saved individually.

    - The entire `data/` directory and required JSON files are automatically created on first run, ensuring the system is ready to use without manual setup.

### Interface/
- Provides a CLI-based menu interface.

- `Menu.py` displays the main navigation and routes actions based on user type (staff or user).

### Models/
- Defines the main domain classes:

    - ``person.py:`` Base class with encrypted password, CPF validation, and masking.

    - ``user.py:`` Extends Person; includes favorites management.

    - ``staff.py:`` Extends Person; includes user/staff/show registration, update and deletion.

    - ``shows.py:`` Represents shows with attributes like name and date.

### Tests/
- Includes unit tests for all major modules:

    - Tests for models (person, user, staff, shows)

    - Tests for system logic (authentication, system, menu)
    Ensures robustness and correctness of the codebase.

## ✅ Current Functionalities

- Staff and user registration with secure password hashing.

- Staff login and management capabilities.

- Show registration, listing, and browsing.

- User login and personalized favorite shows management (stored individually).

- JSON-based persistent storage, with automatic local database creation on first run.

- CLI-based user interface.


## 🧠 Key Concepts

- Object-Oriented Programming (OOP)

- Modular architecture in Python

- Secure password hashing with ``passlib`` library

- Real CPF validation and masking

- CLI-based user interaction

- Separation of logic, interface, and control layers


## 🚧 Upcoming Features

- Graphical User Interface (GUI) integration to enhance user experience.

- Email API integration for automated notifications on key operations such as:

    - Account creation

    - Password changes

    - Show favoriting

    - Upcoming event reminders

- Password input masking during CLI interactions for improved security and privacy.
- Binary search on the ``find_id`` function.


## ▶️ How to Run

1. Make sure you have **Python 3** installed.  
2. Run the main file using:

```bash
python main.py
```

3. Use the terminal prompts to interact with the app like the examples:

    - If this is your first time running the system, use the main staff credentials as shown in the example:
        ```python
        === Login Menu ===
        [1] Login User
        [2] Login Staff
        [0] Exit
        Select an option: 2
        Staff ID: 1
        Password: admin1234

        Staff logged in successfully!

        === Staff Menu | Logged: Admin ===
        [1] Register
        [2] Update
        [3] Remove
        [4] View
        [5] Logout
        [0] Exit System
        Select an option: 
        ```
    
    - If you have already registered a user, you can log in with those credentials as in this example:
        ```python
            === Login Menu ===
            [1] Login User
            [2] Login Staff
            [0] Exit
            Select an option: 1
            User ID: 15
            Password: daniel123

            User logged in successfully!

            === User Menu | Logged: daniel ===
            [1] View all shows
            [2] Add show to favourite
            [3] Remove show from favourite
            [4] View favourite shows
            [5] Logout
            [0] Exit system
            Select an option: 
        ```

## ✍️ Author
- Developed by Daniel de Souza
