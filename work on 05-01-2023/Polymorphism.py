# Method overriding in python with hierarchical inheritance
class Birds:

    def intro(self):
        return 'This is Bird class'

    def fly(self):
        return 'All Birds fly but some not'


class Parrot(Birds):
    color = 'Green'

    def intro(self):
        return f'Parrot color are : {self.color}'

    def fly(self):
        return 'Parrot can fly easily'


class Penguins(Birds):
    color = 'Black & white'

    def intro(self):
        return f'Penguins color are : {self.color}'

    def fly(self):
        return r"Penguins cann't fly"


par = Parrot()
print(f'{par.intro()} \n{par.fly()}')

pen = Penguins()
print(f'{pen.intro()} \n{pen.fly()}')
b = Birds()
print(f'Birds class {b.fly()}')


# Method ovrloading
class FindLen:
    def len(self, data):
        c = 0
        if type(data) == str:
            for i in data:
                c += 1
        elif type(data) == list:
            for i in data:
                c += 1
        return c


if __name__ == '__main__':
    l = FindLen()
    name = 'Harhit'
    print(f'Length of {name} : {l.len(name)}')

    lst = [12, 23, 45, 56, 46]
    print(f'Length of {lst} : {l.len(lst)}')
