from flask import *
from database import dataset
import os
import sqlite3
import base64

app = Flask(__name__)

def append_pic():
    conn = sqlite3.connect("main.db")
    cursor = conn.cursor()
    # cursor.execute("CREATE TABLE cards (Title TEXT, Desc TEXT, Image BLOB)")

    with open(r"C:\Main_Folder\desktop\projs\flash_cards\images\2.jpg", "rb") as img:
        image = img.read()

    title = "F-35"
    desc = "The Lockheed Martin F-35 Lightning II is an American family of single-seat, single-engine, all-weather stealth multirole combat aircraft that is intended to perform both air superiority and strike missions."
    base64_image = base64.b64encode(image).decode('utf-8')

    cursor.execute("INSERT INTO cards VALUES (?, ?, ?)", (title, desc, base64_image))
    conn.commit()
    conn.close()

# append_pic()

def return_data():
    conn = sqlite3.connect("main.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cards")

    cards = cursor.fetchall()
    cards = [list(i) for i in cards]
    return cards

# print(return_data())

@app.route("/")
def home():
    return render_template("index.html", all_data = return_data())

if __name__ == "__main__":
    app.run(debug = True, port = 1313)
