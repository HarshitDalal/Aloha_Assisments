from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def engine(self):
        pass

    @abstractmethod
    def design(self):
        pass


class Car(Vehicle):

    def __init__(self, c_name, name, power, model, color):
        self.c_name = c_name
        self.name, self.power = name, power
        self.model, self.color = model, color

    def engine(self):
        return f'Engine name : {self.name} , power : {self.power}'

    def design(self):
        return f'Model : {self.model} , color : {self.color}'

    def show_detail(self):
        return f'Car : {self.c_name} \n{self.engine()} \n{self.design()}'


if __name__ == '__main__':
    c1 = Car('TATA', 'BS6', '1199c', 'Nexon', 'black')
    print(c1.design())
    print(c1.engine())
    print(c1.show_detail())
