import ZODB
import ZODB.FileStorage


def connect(name='Data.fs'):
    storage = ZODB.FileStorage.FileStorage(name)
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root
    return root
