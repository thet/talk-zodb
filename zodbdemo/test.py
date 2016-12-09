import pdb
pdb.set_trace()

# CONNECT AND ADD

import connect
root = connect.connect()

if not getattr(root, 'mytalk', False):
    root.mytalk = 'ZODB @ PyMNtos'

root.mytalk


# COMMIT THE TRANSACTION

import transaction
transaction.commit()


# Persistent objects in a BTree structure

import model
import BTrees.OOBTree

root.talks = BTrees.OOBTree.BTree()
root.talks['talk1'] = model.Talk(name='David Xu', title='Introduction to Jupyter Notebooks')  # noqa
root.talks['talk2'] = model.Talk(name='Mark Hubenthal', title='Scraping the Discogs database')  # noqa
root.talks['talk3'] = model.Talk(name='Johannes Raggam', title='ZODB - The Zope Object Database')  # noqa


import transaction
transaction.commit()


pass
