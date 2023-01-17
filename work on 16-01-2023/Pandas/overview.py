import pandas as pd

if __name__ == '__main__':

    # DataFrame is a collection of row and column it is one of the data structure in pandas
    data = {
        'name': ['harry', 'harsh', None, 'manku'],
        'age': [23, 22, 23, None],
        'city': ['pune', 'burhanpur', 'pune', None]
    }

    df = pd.DataFrame(data)
    print(df)
    print()

    # Series is a collection of a single column data it is also a data structure of pandas
    data = [i for i in range(1, 21)]
    sr = pd.Series(data, name='Range')
    print(sr.head())
    print()

    # Read data from comma separated value file
    data1 = pd.read_csv('../Files/titanic.csv')
    print(data1.shape)
    d = data1[['Age']]
    print(d.describe())

    print(data1[['Age', 'Fare']].describe())

