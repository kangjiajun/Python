import os
import sqlite3
import functools

class DBInstaller:
    def __init__(self):
        pass
    
    def create(self, dbName, scriptDir):
        conn = sqlite3.connect(dbName)

        sqls = [os.path.join(scriptDir, f) for f in os.listdir(scriptDir) if f.endswith('.sql')]
        run = functools.partial(self.runOneScript, conn)
        map(run, sqls)

        conn.close()

    def runOneScript(self, connection, script):
        print 'run script: ' + script
        cursor = connection.cursor()
        with open(script) as f:
            lines = f.readlines()
            for sql in lines:
                cursor.executescript(sql)
        connection.commit()
        
        

