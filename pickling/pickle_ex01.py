'''Program to illustrate store efficiently using pickle module.

Translates an in-memory python object into a serialized byte stream -
a string of bytes that can be written to any file like object.'''

import pickle

def storeData():
    # Initializing data to be stored in db
    Dhan = {'key' : 'Dhan',
        'name' : 'Dhanu',
        'age' : 21,
        'pay' : 1000}
    Raj = {'key' : 'Raj',
        'name' : 'Raju',
        'age' : 22,
        'pay' : 2000}

    # database
    db = {}
    db['Dhan'] = Dhan
    db['Raj'] = Raj

    # Its important to use binary mode.
    dbfile = open('examplePickle', 'ab')

    # souce, destination
    pickle.dump(db, dbfile)
    dbfile.close()

def loadData():
    # for reading also binary mode is important
    dbfile = open('examplePickle', 'rb')
    db = pickle.load(dbfile)
    for keys in db:
        print (keys, '=>', db[keys])
    dbfile.close()

if __name__ == '__main__':
    storeData()
    loadData()