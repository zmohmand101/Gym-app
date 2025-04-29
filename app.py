from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('gym.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    trainers = conn.execute('SELECT * FROM trainers').fetchall()
    conn.close()
    return render_template('index.html', trainers=trainers)

@app.route('/trainer/<int:trainer_id>')
def trainer_detail(trainer_id):
    conn = get_db_connection()
    trainer = conn.execute('SELECT * FROM trainers WHERE id = ?', (trainer_id,)).fetchone()
    clients = conn.execute('SELECT * FROM clients WHERE trainer_id = ?', (trainer_id,)).fetchall()
    sessions = conn.execute('SELECT * FROM sessions WHERE trainer_id = ?', (trainer_id,)).fetchall()
    total_revenue = sum(session['price'] for session in sessions)
    conn.close()
    return render_template('trainer.html', trainer=trainer, clients=clients, sessions=sessions, revenue=total_revenue)

if __name__ == '__main__':
    app.run(debug=True)
