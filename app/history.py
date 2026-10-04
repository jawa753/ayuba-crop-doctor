import sqlite3
import os
from datetime import datetime


# ============================================================
# AYUBA CROP DOCTOR
# Prediction History Database
# ============================================================

DATABASE_PATH = os.path.join(
    os.path.dirname(
        os.path.abspath(__file__)
    ),
    "prediction_history.db"
)


# ============================================================
# DATABASE CONNECTION
# ============================================================

def get_connection():

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    connection.row_factory = sqlite3.Row

    return connection


# ============================================================
# CREATE DATABASE TABLE
# ============================================================

def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS predictions (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            date_time TEXT NOT NULL,

            crop TEXT NOT NULL,

            prediction TEXT NOT NULL,

            confidence REAL NOT NULL

        )
        """
    )

    connection.commit()

    connection.close()


# ============================================================
# SAVE PREDICTION
# ============================================================

def save_prediction(
    crop,
    prediction,
    confidence
):

    connection = get_connection()

    cursor = connection.cursor()

    date_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    cursor.execute(
        """
        INSERT INTO predictions
        (
            date_time,
            crop,
            prediction,
            confidence
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            date_time,
            crop,
            prediction,
            confidence
        )
    )

    connection.commit()

    connection.close()


# ============================================================
# GET PREDICTION HISTORY
# ============================================================

def get_prediction_history():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            id,
            date_time,
            crop,
            prediction,
            confidence
        FROM predictions
        ORDER BY id DESC
        """
    )

    records = cursor.fetchall()

    connection.close()

    return records


# ============================================================
# CLEAR PREDICTION HISTORY
# ============================================================

def clear_prediction_history():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM predictions
        """
    )

    connection.commit()

    connection.close()


# ============================================================
# DATABASE TEST
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("AYUBA CROP DOCTOR")
    print("PREDICTION HISTORY DATABASE")
    print("=" * 60)

    initialize_database()

    print()
    print("Database initialized successfully.")
    print()
    print(
        f"Database location:"
    )
    print(
        DATABASE_PATH
    )

    print()
    print(
        "Prediction history system ready."
    )

    print("=" * 60)