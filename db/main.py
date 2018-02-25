import os
import sqlite3

def main():
    conn = sqlite3.connect('major.db')
    cursor = conn.cursor()

    cursor.execute('''create table Car_Info (
        Model TEXT primary key,
        Brand TEXT,
        StartingPrice INTEGER);
        ''')
    conn.commit()

    carInstallFile = os.path.join("scripts", "CarInstall.sql")
    with open(carInstallFile) as f:
        lines = f.readlines()
        for sql in lines:
            cursor.executescript(sql)
    conn.commit()

    conn.close()


if __name__ == '__main__':
    main()


