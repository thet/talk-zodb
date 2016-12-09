===============================
ZODB - The Zope Object DataBase
===============================

Who am I
========

- Johannes Raggam
- Graz / Austria (Map)
- Plone CMS core developer
- https://github.com/thet/
- https://twitter.com/thetetet


What is the ZODB
================

- Zope Object DataBase

- Stores Python objects

- Pickles

- Transactional

- Fullfills ACID with Snapshot Isolation

- Multiple clients via ZEO

- Replications via ZRS


What is it good for?
====================

- Easy to use Python database.

- Embedable.

- Applications with complex relationships and data structures.

- Scalable - 100GB of data, no problem.

- Mature - since 1996.


What is it not so good for?
===========================

- High write volume.

- Caching not an option.

- Need for non Python standard tools to access data.


What is it used for?
====================

- Zope Object Publishing Environment - ZOPE

- Perfect for hierarchical Data,

- Perfect for CMS - Plone.

- Default storage layer for Pyramid


ZODB Example
============

....


Thanks!
=======




- Storage of Assembled Objects
  In comparison to ORM mappers
    Less expensive, both conceptionally and performance wise

- Objects are stored in a hierarchy under a root object.

    - Root object acts like a Python dictionary.
    
    - Nice for CMS: hierarchical structure of content, content within folders, Plone!

- Schema Less - add or remove instance attributes as you like.
  - Only restriction: Everything has to be pickle-able
  - Still, you can use schemas (CMS Types).

- Easy to use, no abstraction between storage and application

- Provides basic persistance and little else

- Security and cataloging must be provided by the application layer
  - Database clients must be trusted.

- Indexing


Example
=======

::
    # myzodb.py

    from ZODB import FileStorage, DB
    import transaction

    class MyZODB(object):
        def __init__(self, path):
            self.storage = FileStorage.FileStorage(path)
            self.db = DB(self.storage)
            self.connection = self.db.open()
            self.dbroot = self.connection.root()

    def close(self):
        self.connection.close()
        self.db.close()
        self.storage.close()


...

- store attributes on root
- fetch

- store complex attributes (dict, list) on root
- use _p_changd

- store objects
- fetch

- store complex..


Mantainance
===========

- ZODB pack
- ZEO
- ZRS




Resources
=========

- https://www.ibm.com/developerworks/aix/library/au-zodb/ (15 April 2008)
- http://blog.startifact.com/posts/older/a-misconception-about-the-zodb.html

https://github.com/zopefoundation/ZODB

http://www.zodb.org/en/latest/
https://github.com/zopefoundation/zodb/blob/master/doc/index.rst
http://www.zodb.org/en/latest/tutorial.html
http://www.zodb.org/en/latest/guide/index.html
http://www.zodb.org/en/latest/reference/index.html
http://www.zodb.org/en/latest/articles/index.html
http://zodb.readthedocs.io/en/latest/introduction.html


https://en.wikipedia.org/wiki/Zope_Object_Database

https://pypi.python.org/pypi/ZODB/5.1.1#new-features

http://docs.plone.org/develop/plone/persistency/database.html#visualizing-object-graphs

https://www.ibm.com/developerworks/aix/library/au-zodb/

























