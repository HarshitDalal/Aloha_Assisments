from datetime import datetime


class Company(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance.c_name = kwargs['c_name']
            cls._instance.c_type = kwargs['c_type']
            cls._instance.c_location = kwargs['c_location']
            cls._instance.creation = datetime.utcnow()
        return cls._instance


if __name__ == '__main__':
    c1 = Company(c_name='aloha', c_location='pune', c_type='it')
    print(c1.c_name)
    c2 = Company(c_name='tcs', c_location='pune', c_type='it')

    print(c2.c_name)
