from msdb import employee, company


# from pgdb.employee import Employee
# from pgdb.company import Company


if __name__ == '__main__':
    e1 = employee.Employee()
    print(e1)
    e1.add('Harshit Dalal', 'harshitdalal21@gmail.com', '+917049530992', 1)
    e1.save()
    print(e1.all_data())
