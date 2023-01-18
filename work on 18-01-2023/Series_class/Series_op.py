import numpy as np
import pandas as pd


class Ser:

    def __init__(self):
        # self.arr1 = np.array(np.random.randint(10, 100, 10))
        self.arr1 = [1, 2, 3, 4, 2, 4, 5, 6, 2, 1]
        self.arr2 = np.array(np.random.randint(20, 200, 10))

    def create_series(self, data):
        ser = pd.Series(data)
        return ser

    def series_to_dataframe(self, **ser):
        df = pd.DataFrame(ser)
        return df

    def find_std(self, df):
        std = df.std()
        return std

    def val_count_series(self, ser, **kwargs):
        val_co = ser.value_counts(**kwargs)
        return val_co

    def change_type(self, ser, type):
        return ser.astype(dtype=type)

    def __del__(self):
        pass


if __name__ == '__main__':
    obj = Ser()
    info1 = obj.create_series(obj.arr1)
    info2 = obj.create_series(obj.arr2)
    df = obj.series_to_dataframe(info1=info1, info2=info2)
    print(f'standard deviation -\n{obj.find_std(df)}\n')

    print(obj.val_count_series(info1, normalize=True, sort=True))
