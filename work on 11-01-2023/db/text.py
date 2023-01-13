# from msdb import employee, company
from pgdb import employee, company

if __name__ == '__main__':
    e1 = employee.Employee()
    print(e1)
    name, email, phone, cid = input().split(',')
    e1.add('Harshit Dalal', 'harshitdalal21@gmail.com', '+917049530992', 1)
    print(e1.all_data())

