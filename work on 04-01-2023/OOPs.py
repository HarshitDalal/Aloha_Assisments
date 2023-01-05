class MyClass:
    '''First class creation'''

    name = 'Harry'

    def fun(self):
        return self.name + ' is boy.'


obj = MyClass()
print(f'Class variable : {obj.name}')
print(f'Member Function : {obj.fun()}')
print()


# class with constructor and representation of the object
class Employee:
    '''Employee class that take 2 Arguments name and age'''

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def show(self) -> str:
        return f'Emp detail Name : {self.name} Age : {self.age}'

    def __str__(self) -> str:
        return f'Employee {self.name}'


# name, age = input("Enter name & age : ").split()
name, age = ('Harry', 20)
emp1 = Employee(name, int(age))
print(emp1.show())
print(emp1)
print()


class Company:
    '''Company class that store detail about companies'''

    __type = 'IT'  # private class variable

    def __init__(self, name: str, loc: str) -> None:
        self.c_name = name
        self.location = loc

    @classmethod
    def changeType(cls, type_name: str) -> None:
        '''Class method to change private class variable from the outside of the class Company'''

        cls.__type = type_name

    @classmethod
    def showType(cls) -> str:
        return 'Company type is : ' + cls.__type

    def companyDetail(self) -> str:
        return f'Company name : {self.c_name}, location : {self.location}, type : {self.__type}'


c1 = Company('Aloha Technology', 'Pune')
c2 = Company('Airtal', 'Mumbai')
print(c1.companyDetail())
print(f'Aloha {c1.showType()}')
# print(c1.type)    # getting error
print(c2.companyDetail())
print(f'Before changes Airtal {c2.showType()}')
# print(c2.type)    # getting error
c1.changeType('Communication')
print(f'After changes Airtal {c2.showType()}')
print()
