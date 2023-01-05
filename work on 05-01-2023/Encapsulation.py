# Encapsulation in python
# private variable and getter setter method
from random import randrange


class Bank:
    bank_name = "SBI"

    def __init__(self, a_name, id):
        self.a_name = a_name
        self.id = id
        self.__bal = 0

    @property
    def balance(self):
        return self.__bal

    @balance.setter
    def balance(self, balance):
        self.__bal += balance if balance > 0 else 0

    def show_detail(self):
        return f'Bank : {self.bank_name}, Name : {self.a_name}, Id : {self.id} , Balance : {self.__bal}'


if __name__ == '__main__':
    id = randrange(0000, 9999)
    c1 = Bank('Harshit', id)
    c1.balance = 2000
    print(c1.show_detail())
    print(f'{c1.a_name} balance is {c1.balance}')
