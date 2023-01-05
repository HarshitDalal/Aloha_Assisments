# Implements all types of inheritance

class Company:
    def __init__(self, c_name, loc, c_type):
        self.c_name, self.loc, self.c_type = c_name, loc, c_type

    def show_company_details(self):
        return f'Company name : {self.c_name} , location : {self.loc}, type : {self.c_type}'


class Employee(Company):
    def __init__(self, e_name, age, c_name, loc, c_type):
        super().__init__(c_name, loc, c_type)
        self.e_name = e_name
        self.age = age
        self.edu = []

    def add_edu(self, *edu):
        self.edu += edu

    def show_emp_details(self):
        return f'Employee name : {self.e_name}, age : {self.age}, education : {self.edu}, {self.show_company_details()}'

if __name__ == '__main__':

    e1 = Employee('Harshit Dalal', 23, 'Aloha Technology', 'Pune', 'IT')
    e1.add_edu('10th', '12th', 'BCA', 'MCA')
    print(e1.show_company_details())
    print(e1.show_emp_details())
    print(f'Employee education : {e1.edu}')
