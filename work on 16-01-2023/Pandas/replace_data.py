import pandas as pd

class Replace:

    def __init__(self):
        self.file = '../Files/titanic.csv'
        self.data = pd.read_csv(self.file)

    def show(self):
        print(self.data.info())
        print(self.data.to_string())

    def replace_by_mean(self, col):
        x = self.data[col].mean()
        new_data =  self.data[col].fillna(x)
        print(new_data.to_string())



if __name__ == '__main__':
    r = Replace()
    r.replace_by_mean('Age')
    r.show()