import sqlite3
from db.database import create_connection

def add_patient(name, age, diagnosis):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO patients (name, age, diagnosis) VALUES (?, ?, ?)", (name, age, diagnosis))
    conn.commit()
    conn.close()
 

def get_all_patients():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_patient(patient_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM patients WHERE id=?", (patient_id,))
    conn.commit()
    conn.close()
    