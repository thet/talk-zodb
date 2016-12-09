import pdb
pdb.set_trace()

# CONNECT AND ADD

import connect
root = connect.connect()

print(getattr(root, 'mytalk', None))
print(getattr(root, 'alltallks', None))


root.mytalk = 'ZODB @ PyMNtos'


# COMMIT THE TRANSACTION

import transaction
transaction.commit()


# SPECIAL CASE WITH LISTS AND DICTS

root.othertalk = 'Scraping the Discogs database'
root.othertalk2 = 'Introduction to Jupyter Notebooks'

root.alltallks = [root.mytalk]

import transaction
transaction.commit()

root.alltallks = root.alltallks + [root.othertalk, root.othertalk2]

import transaction
transaction.commit()






pass
