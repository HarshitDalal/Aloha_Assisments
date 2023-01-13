class Creation:
    __instance = {}

    def __init__(self, name):
        if name not in self.__instance:
            self.__instance[name] = self
        else:
            raise Exception(f'Object already exists')

    @staticmethod
    def instance(name):
        if name not in Creation.__instance:
            Creation(name)
        return Creation.__instance[name]

    def __del__(self):
        print('cre')


class Company(Creation):

    def __init__(self, c_name):
        super().__init__(c_name)
        self.c_name = c_name
        self.__c_type = ''
        self.__c_location = ''
        self.__employees = []

    def type(self, c_type=None):
        if c_type is None:
            return self.__c_type
        else:
            self.__c_type = c_type

    def location(self, c_location=None):
        if c_location is None:
            return self.__c_location
        else:
            self.__c_location = c_location

    def add_employee(self, e_obj):
        self.__employees.append(e_obj)

    def show_employee(self):
        return self.__employees

    def __repr__(self):
        return f'Company(c_name={self.c_name}, type={self.__c_type}, location={self.__c_location}, employee={self.__employees}'

    def __del__(self):
        print('com')


class Employee:
    def __init__(self, e_name):
        self.e_name = e_name

    def __repr__(self):
        return f'Employee(e_name={self.e_name})'

    def __del__(self):
        print("emp")


class Register:
    def __init__(self):
        self.__register_com = {}

    def add_c(self, c_name, c_obj):
        self.__register_com[c_name] = c_obj

    def remove_c(self, c_name):
        remove_com = self.__register_com.pop(c_name)
        return f'{remove_com} remove'

    def __repr__(self):
        return f'Register Companies {self.__register_com}'

    def __del__(self):
        print('reg')


if __name__ == '__main__':
    aloha = Company('aloha')
    tata = Company('tata')
    e1 = Employee('harry')
    aloha.add_employee(e1)
    aloha.type('IT')
    aloha.location('Pune')
    print(aloha)
