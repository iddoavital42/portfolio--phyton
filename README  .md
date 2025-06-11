# 🏥 Clinic Management System

A simple clinic management system built with **Python**, using:

- 📦 Flask – for the backend REST API  
- 🧱 SQLite – for storing patient data  
- 🖥 Tkinter – for the graphical user interface (GUI)

---

## 🚀 Features

- View all patients
- Add new patients
- Delete patients
- GUI for easy interaction
- Backend API for future integration

---

## 📂 Project Structure

```
clinic-system/
│
├── app.py                      # Flask backend
├── clinic_ui.py                # Tkinter GUI interface
├── controllers/
│   └── patient_controller.py   # Logic for handling patients
├── db/
│   └── database.py             # SQLite DB connection + table setup
└── README.md                   # This file
```

---

## 🔧 Installation

1. Clone the project:

   ```bash
   git clone https://github.com/your-username/clinic-system.git
   cd clinic-system
   ```

2. Install required packages:

   ```bash
   pip install flask requests
   ```

---

## 💡 Usage

1. Run the Flask server:

   ```bash
   python app.py
   ```

2. In another terminal, run the GUI:

   ```bash
   python clinic_ui.py
   ```

---

## 📬 API Endpoints

- `GET /patients` – Get list of all patients  
- `POST /patients` – Add a new patient  
- `DELETE /patients/<id>` – Delete patient by ID  

---

## 🧠 Notes

- Database is created automatically (`clinic.db`) inside the `db/` folder.
- All operations are stored in SQLite – no setup needed.

---

## ✨ Future Improvements

- Add update/edit patient
- Add search functionality
- Add login & authentication

---

## 🧑‍💻 Author

Created by [Iddo Avital](https://github.com/your-username) as part of a professional portfolio project.
