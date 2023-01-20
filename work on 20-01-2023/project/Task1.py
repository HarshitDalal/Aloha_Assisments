from datetime import datetime
import numpy as np
import pandas as pd


class WorkOnEmployee:

    def __init__(self):
        self.__start = datetime.now()
        self.__path = '../Files/'
        self.data = pd.read_json(self.__path + 'UserData.json')

    def show_data(self):
        print(self.data.to_string())

    @staticmethod
    def __verify(df1):
        # emails = ['verified' for em in df1['email'] if em != np.nan else 'not_verified']
        emails = []
        for em in df1['email']:
            if em is np.nan:
                emails.append('not_verified')
            else:
                emails.append('verified')
        return emails

    def __names_of_column(self, col):
        column = tuple(self.data.columns.values)
        return column.index(col)

    def process(self):
        df1 = pd.DataFrame()
        df1['email'] = self.data['email']
        email_status = self.__verify(df1)
        self.data.insert(self.__names_of_column('email') + 1, 'email_status', email_status)

    def save_data(self):
        self.data.to_csv(self.__path + 'UserData.csv')

    def __del__(self):
        end = datetime.now()
        diff = end - self.__start
        print(f'Process takes {diff} time')


if __name__ == '__main__':
    obj = WorkOnEmployee()
    obj.process()
    # obj.show_data()
    obj.save_data()
