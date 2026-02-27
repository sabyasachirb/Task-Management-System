# 🗂️ Task Management System

A Django-based **multi-user Task Management System** that allows users to create, categorize, edit, complete, and manage tasks with secure authentication and clean architecture.

---

## 🚀 Features

- 🔐 **User Authentication & Authorization**
  - User registration, login, logout
  - Password change 
  - User-specific task access (no data leakage)

- 📝 **Task Management**
  - Create, edit, delete, and complete tasks
  - Mark tasks as completed with conditional UI behavior
  - Completed tasks cannot be edited or deleted

- 🏷️ **Category Management**
  - Tasks can belong to **multiple categories**
  - Categories can be reused across tasks
  - Implemented using Django Many-to-Many relationships

- 📋 **Clean Forms & Validation**
  - Used **Django ModelForms** for form handling
  - Server-side validation and error handling

- 🎨 **Responsive UI**
  - Built with **Bootstrap**
  - Task display using Bootstrap cards
  - Conditional rendering based on task status

- 🧱 **Scalable Architecture**
  - Separate Django apps for `task` and `category`
  - Global base template with reusable components
  - App-specific templates for better maintainability

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Database:** SQLite (Development)
- **Frontend:** HTML, Bootstrap
- **ORM:** Django ORM
- **Authentication:** Django built-in auth system

---

## 🧠 Key Technical Highlights

- Designed and implemented a **multi-user task management system** with authentication and role-based access.
- Modeled **Many-to-Many relationships** between tasks and categories using Django ORM.
- Implemented **secure CRUD operations** with proper authorization and error handling using `get_object_or_404`.
- Used **ModelForms** for validation and dynamic form rendering.
- Integrated **Bootstrap UI** with conditional rendering based on task completion status.
- Followed **clean app-based architecture** and reusable template design.

---


