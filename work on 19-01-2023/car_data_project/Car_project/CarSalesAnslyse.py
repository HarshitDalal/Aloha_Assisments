import pandas as pd
from datetime import datetime


class CarSales:

    def __init__(self):
        self.__start = datetime.now()
        self.__car = pd.read_csv('../dataFiles/car_sale.csv')

    def showAllData(self):
        return self.__car.to_string()

    def rangeData(self, start, end):
        return self.__car[start:end].to_string()

    def replaceNullToMean(self, col):
        mean_val = self.__car[col].mean()
        self.__car[col].fillna(mean_val, inplace=True)

    def replaceNullToMedian(self, col):
        median_val = self.__car[col].median()
        self.__car[col].fillna(median_val, inplace=True)

    def replaceNullToMode(self, col):
        mode_val = self.__car[col].mode()[0]
        self.__car[col].fillna(mode_val, inplace=True)

    def findNullValuesCol(self):
        values = self.__car.isnull().sum()
        with open('../dataFiles/NullValueStatus.txt', 'a') as f:
            f.writelines(str(values))
            f.write('\n________________________________________________\n')
        return values

    def namesOfColumns(self):
        column = tuple(self.__car.columns.values)
        return column

    def namesOfAllNumeric(self):
        columns = self.__car._get_numeric_data().columns.values.tolist()
        return columns

    def saveFile(self, filename):
        self.__car.to_csv('../dataFiles/' + filename)
        print('File save with changes')

    def __repr__(self):
        return 'performing data science operation on car sales dataset'

    def __del__(self):
        end = datetime.now()
        diff = end - self.__start
        print(f'\n\ntotal time taken by all operations is {diff}')


def main():
    obj = CarSales()
    columns = obj.namesOfColumns()
    num_col = obj.namesOfAllNumeric()
    for col in num_col:
        obj.replaceNullToMean(col)
    print(obj.findNullValuesCol())
    # print(obj.rangeData(12, 25))
    print(obj.saveFile('carMean.csv'))

if __name__ == '__main__':
    main()
