# library-management-system
a system which makes work easier for student and librarian (we can also make this type of systems for any purposes and also integrate agents with them which make our works even more easier)
# Library Management System

A full-stack web-based Library Management System built with Python and Flask, featuring user authentication, inventory/book tracking with cover uploads, SQLite database integration, and WhatsApp notification capabilities.

## 🎯 Use Purpose

The primary purpose of this project is to digitize and streamline library operations. It allows administrators and users to manage book records, handle user authentication (login/signup), track book inventories, upload media/covers, and send automated notifications or reminders via WhatsApp.

## 🛠️ Tools & Tech Stack

* **Programming Language:** Python
* **Backend Framework:** Flask (`app.py`)
* **Database:** SQLite (`library.db`)
* **Messaging Integration:** WhatsApp Helper (`whatsapp_helper.py`)
* **Frontend/UI:** HTML Templates (`index.html`, `login.html`, `register.html`) with Static Assets

## ✨ Features

* **🔐 User Authentication:** Secure login and registration system (`login.html`, `register.html`) to manage system access.
* **📚 Book & Inventory Management:** Add, update, and manage book collections seamlessly.
* **🖼️ Media & Cover Uploads:** Support for uploading and storing book cover images and media files (`static/uploads/`).
* **💬 WhatsApp Notifications:** Integrated WhatsApp helper module to automate alerts, reminders, or messages to library members (`whatsapp_helper.py`).
* **🗄️ Persistent Storage:** Uses a lightweight SQLite database (`library.db`) managed via dedicated database modules (`database.py`).
* **💻 Web Interface:** Clean HTML template structure for dashboard, home page, and user workflows.

## 📂 Project Structure

```text
library_management_system/
├── app.py                      # Main Flask application entry point
├── database.py                 # Database connection and query handlers
├── gui.py                      # Graphical interface / desktop wrapper components
├── whatsapp_helper.py          # WhatsApp messaging integration script
├── library.db                  # SQLite database file for persistent storage
├── static/
│   └── uploads/                # Directory for uploaded book covers and images
└── templates/
    ├── index.html              # Main dashboard / home page template
    ├── login.html              # User login page template
    └── register.html           # User registration page template
