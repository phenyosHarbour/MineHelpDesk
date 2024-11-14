import sqlite3

def create_database():
    conn = sqlite3.connect('support_db.sqlite')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY,
            name TEXT,
            department TEXT,
            workstation TEXT,
            description TEXT,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_ticket(name, department, workstation, description):
    conn = sqlite3.connect('support_db.sqlite')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tickets (name, department, workstation, description, status)
        VALUES (?, ?, ?, ?, 'Pending')
    ''', (name, department, workstation, description))
    conn.commit()
    conn.close()

def update_ticket_status(ticket_id, status):
    conn = sqlite3.connect('support_db.sqlite')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE tickets
        SET status = ?
        WHERE id = ?
    ''', (status, ticket_id))
    conn.commit()
    conn.close()

def delete_ticket(ticket_id):
    conn = sqlite3.connect('support_db.sqlite')
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM tickets
        WHERE id = ?
    ''', (ticket_id,))
    conn.commit()
    conn.close()
