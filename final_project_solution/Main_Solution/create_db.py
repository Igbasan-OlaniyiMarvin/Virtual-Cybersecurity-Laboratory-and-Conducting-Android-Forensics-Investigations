import sqlite3

def create_extended_db():
    conn = sqlite3.connect("sample_sms.db")
    cursor = conn.cursor()

    # SMS Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        address TEXT NOT NULL,
        date TEXT NOT NULL,
        body TEXT NOT NULL
    )
    ''')

    # Call Logs Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS call_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number TEXT NOT NULL,
        type TEXT NOT NULL,
        duration TEXT,
        date TEXT NOT NULL
    )
    ''')

    # Browser History Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS browser_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT NOT NULL,
        title TEXT,
        visit_time TEXT NOT NULL
    )
    ''')

    # Sample SMS
    sms_data = [
        ('+2347012345678', '2023-12-01 10:30:00', 'Hello, how are you?'),
        ('+2348023456789', '2023-12-01 10:45:00', 'Your OTP is 345678'),
        ('+2348098765432', '2023-12-02 09:15:00', 'Meeting postponed till tomorrow.'),
        ('+2347055550000', '2023-12-02 21:12:00', 'Send the documents by email.'),
        ('+2348181234567', '2023-12-03 15:50:00', 'Thanks for reaching out.')
    ]

    call_logs = [
        ('+2347012345678', 'incoming', '60', '2023-12-01 09:00:00'),
        ('+2348023456789', 'missed', '', '2023-12-02 11:45:00'),
        ('+2348098765432', 'outgoing', '120', '2023-12-03 17:30:00')
    ]

    browser_history = [
        ('https://example.com', 'Example Site', '2023-12-01 08:45:00'),
        ('https://mail.com', 'Mail Homepage', '2023-12-02 10:20:00'),
        ('https://news.ng', 'Naija News', '2023-12-03 12:05:00')
    ]

    cursor.executemany('INSERT INTO sms (address, date, body) VALUES (?, ?, ?)', sms_data)
    cursor.executemany('INSERT INTO call_logs (number, type, duration, date) VALUES (?, ?, ?, ?)', call_logs)
    cursor.executemany('INSERT INTO browser_history (url, title, visit_time) VALUES (?, ?, ?)', browser_history)

    conn.commit()
    conn.close()
    print("Database with SMS, call logs, and browser history created.")

if __name__ == "__main__":
    create_extended_db()
