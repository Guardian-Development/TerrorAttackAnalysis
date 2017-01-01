import sys
from database import dbaccessor
from database import attackmodel
from filereader import csvreader

def addCsvFileToDb():
    global db
    db = dbaccessor.DatabaseAccessor("terrordb", "globalattacks")
    csvreader.readCsvFile('globalterrorismdb_0616dist.csv', convertAndSubmitToDb)
    return

def convertAndSubmitToDb(attack):
    model = attackmodel.buildAttack(
        attack[0],
        attack[1],
        attack[2],
        attack[3],
        attack[7],
        attack[8],
        attack[9],
        attack[10],
        attack[11],
        attack[12],
        attack[13],
        attack[14],
        attack[18])
    try:
        id = db.insertDocument(model)
        print(id)
    except Exception as e:
        print("could not convert to utf-8 so skipped")

    return

if __name__ == '__main__':
    sys.exit(addCsvFileToDb())
