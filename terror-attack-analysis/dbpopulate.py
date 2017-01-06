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
        attack[0], #eventId
        attack[1], #year
        attack[2], #month
        attack[3], #day
        attack[7], #countryId
        attack[8], #countryName
        attack[9], #regionId
        attack[10], #regionName
        attack[11], #state
        attack[12], #city
        attack[13], #latitude
        attack[14], #longitude
        attack[18], #description
        attack[34], #targetId
        attack[35], #targetDescription
        attack[100], #kill count
        attack[99]) #weapon used
    try:
        id = db.insertDocument(model)
        print(id)
    except Exception as e:
        print("could not convert to utf-8 so skipped")

    return

if __name__ == '__main__':
    sys.exit(addCsvFileToDb())
