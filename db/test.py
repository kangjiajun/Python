import sqlite3

def main():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('''create table CarInfo
    (Name INT,
    Price INT);''')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()


