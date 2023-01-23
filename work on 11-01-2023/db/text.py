# from msdb import employee, company
from pgdb import employee, company

if __name__ == '__main__':
    e1 = employee.Employee('db_config_using_python')
    print(e1)
    # name, email, phone, cid = input().split(',')
    e1.add('kapil Pandya', 'kapilpandya1310@gmail.com', '+919098983216', 4)
    print(e1.all_data())
    # c1 = company.Company('db_config_using_python')
    # print(c1)
    # c1.add('Hexaview', 'IT', 'Pune')
    # print(c1.all_data())

