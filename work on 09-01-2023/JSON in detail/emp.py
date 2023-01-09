import json


class OperationOnJson:

    def __init__(self):
        self.file = open('emp.json', 'r+')

    def read_data(self):
        return f'Details of Employee {self.file.readlines()}'

    def get_detail_by_id(self, employeeCode: str):
        emp_data = self.file.read()
        data = json.loads(emp_data)
        for emp in data['Employees']:
            if emp['employeeCode'] == employeeCode:
                return f'{emp["preferredFullName"]} job title is {emp["jobTitleName"]}'
        return 'No Employee found'

    def update_data(self, employeeCode: str):
        emp_data = self.file.read()
        data = json.loads(emp_data)
        for emp in data['Employees']:
            if emp['employeeCode'] == employeeCode:
                pass

    def __del__(self):
        self.file.close()


if __name__ == '__main__':
    ob = OperationOnJson()
    ob.get_detail_by_id("E1")
