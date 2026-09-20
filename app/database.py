import sqlite3
from datetime import datetime


def get_db():
    connection = sqlite3.connect("leads.db")
    connection.row_factory = sqlite3.Row
    return connection


def init_db(app):
    with app.app_context():
        connection = get_db()
        connection.execute("""
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                isim TEXT NOT NULL,
                telefon TEXT NOT NULL,
                mesaj TEXT,
                tarih TEXT NOT NULL
            )
        """)
        connection.commit()
        connection.close()


def lead_ekle(isim, telefon, mesaj=""):
    connection = get_db()
    connection.execute(
        "INSERT INTO leads (isim, telefon, mesaj, tarih) VALUES (?, ?, ?, ?)",
        (isim, telefon, mesaj, datetime.now().isoformat())
    )
    connection.commit()
    connection.close()


def tum_leadler():
    connection = get_db()
    leads = connection.execute(
        "SELECT * FROM leads ORDER BY id DESC"
    ).fetchall()
    connection.close()
    return [dict(lead) for lead in leads]