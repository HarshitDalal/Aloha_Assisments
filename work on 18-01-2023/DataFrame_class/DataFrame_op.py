import pandas as pd
import numpy as np


class OperationsOnCsv:

    def __init__(self, filename):
        self.__filepath = '../Files/'
        self.data = pd.read_csv(self.__filepath + filename)

    def remove_duplicate(self):
        self.data.drop_duplicates(inplace=True)

    def add_zero_if_nan(self, col, value):
        self.data[col].fillna(value, inplace=True)

    def re_format_MF(self, col):
        # self.data[col] = self.data[col].apply({'male': 'M', 'female': 'F'}.get)
        self.data[col].replace(['male', 'female'], ['M', 'F'], inplace=True)

    def replace_NaN_0(self):
        self.data.fillna(0, inplace=True)

    def save_to_csv(self, filename):
        self.data.to_csv(self.__filepath + filename)

    def save_to_excel(self, filename):
        self.data.to_excel(self.__filepath + filename)

if __name__ == '__main__':
    obj = OperationsOnCsv('titanic.csv')
    # print(obj.data.to_string())
    obj.re_format_MF('Sex')
    obj.replace_NaN_0()
    # obj.add_zero_if_nan('Survived', 0.0)
    # obj.add_zero_if_nan('Age', 0.0)
    # obj.add_zero_if_nan('SibSp', 0)
    print(obj.data.to_string())
    # obj.save_to_csv('updated_titanic.csv')
    obj.save_to_excel('updated_titanic.xlsx')

