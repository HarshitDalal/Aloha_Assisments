import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv('../Files/titanic.csv')
    # print(data.to_string())
    # print(data.head(20).to_string())
    # print(data.describe().to_string())
    # print(data.mean(numeric_only=True))
    # print(data.median(numeric_only=True))
    #
    # print(data[['Age', 'Class']].mode(numeric_only=True))
    # print(data.max(numeric_only=True))
    # print(data.min(numeric_only=True))
    print(data.corr(numeric_only=True).to_string())
