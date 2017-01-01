import sys
from database import dbaccessor
from database import attackmodel

def main():
    db = dbaccessor.DatabaseAccessor("terrordb", "globalattacks")
    model = attackmodel.buildAttack(1, 2016, 9, 21)
    print(model)
    insertedId = db.insertDocument(model)
    print(insertedId)
    return


if __name__ == '__main__':
    sys.exit(main())
