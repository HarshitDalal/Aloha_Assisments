class AlohaSingleTon(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            cls.__instance.__location = ''
            cls.__instance.__capacity = 0
        return cls.__instance

    def add_location(self, location):
        self.__location = location

    def add_capacity(self, capacity):
        self.__capacity = capacity

    def __repr__(self):
        return f'Aloha(location={self.__location}, capacity={self.__capacity})'

    def __del__(self):
        pass


class AlohaNormal(object):

    def __init__(self):
        self.__location = ''
        self.__capacity = 0

    def add_location(self, location):
        self.__location = location

    def add_capacity(self, capacity):
        self.__capacity = capacity

    def __repr__(self):
        return f'Aloha(location={self.__location}, capacity={self.__capacity})'

    def __del__(self):
        pass


if __name__ == '__main__':
    a1 = AlohaSingleTon()
    a2 = AlohaSingleTon()
    a2.add_location('pune')
    print(a1, a2)

    a1 = AlohaNormal()
    a2 = AlohaNormal()
    a1.add_location('pune')
    print(a1, a2)
