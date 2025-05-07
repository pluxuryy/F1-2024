import os
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('f1_2024.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    drivers_count = conn.execute('SELECT COUNT(*) FROM Drivers').fetchone()[0]
    teams_count = conn.execute('SELECT COUNT(*) FROM Teams').fetchone()[0]
    tracks_count = conn.execute('SELECT COUNT(*) FROM Tracks').fetchone()[0]
    conn.close()
    return render_template('index.html', drivers_count=drivers_count, 
                           teams_count=teams_count, tracks_count=tracks_count)



@app.route('/drivers')
def drivers():
    conn = get_db_connection()
    drivers = conn.execute('SELECT * FROM Drivers ORDER BY points DESC').fetchall()
    conn.close()
    return render_template('drivers.html', drivers=drivers)


@app.route('/teams')
def teams():
    conn = get_db_connection()
    teams = conn.execute('SELECT * FROM Teams ORDER BY team_points DESC').fetchall()
    conn.close()
    return render_template('teams.html', teams=teams)

@app.route('/tracks')
def tracks():
    conn = get_db_connection()
    tracks = conn.execute('SELECT * FROM Tracks').fetchall()
    conn.close()
    return render_template('tracks.html', tracks=tracks)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

#https://f1-2024-dashboard.onrender.com

