import os
from DBInstaller import *

def main():
    dbName = 'Car.db'
    if not os.path.exists(dbName):
        DBInstaller().create(dbName, './scripts/install')
    else:
        print dbName + ' already exist'

if __name__ == '__main__':
    main()


