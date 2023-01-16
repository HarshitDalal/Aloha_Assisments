"""
Reference from stackoverflow
"""

class DBConnector(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DBConnector, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        # your db connection code in constructor
        pass


con = DBConnector()
con1 = DBConnector()
con is con1  # output is True
