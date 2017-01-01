from pymongo import MongoClient

class DatabaseAccessor(object):

    client = MongoClient('mongodb://localhost:27017/')
    databaseName = ''
    tableName = ''

    def getAll(self):
        return self.getTable().find()

    # get a document by its given db _id
    def getDocumentById(self, id):
        return self.getTable().find_one({"_id": id})

    # insert a document for the specified db and table
    def insertDocument(self, document):
        document_id = self.getTable().insert_one(document).inserted_id
        return document_id

    # gets the current table being used for storage
    def getTable(self):
        return self.client[self.databaseName][self.tableName]

    # sets the MongoDB dbname to connect to, and the specific table to use
    def __init__(self, dbName, tbName):
        self.databaseName = dbName
        self.tableName = tbName
