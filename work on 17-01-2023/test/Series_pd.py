import pandas as pd
import numpy as np

if __name__ == '__main__':
    info = np.array(['harry', 'manku', 'kapu', 'harsh'])
    data = pd.Series(info)
    print(data)

    info = {'harry': 500, 'manku': 300, 'kapu': 600, 'harsh': 200}
    data = pd.Series(info)
    print(data)

    # print(data.index)
    # print(data.shape)
    # print(data.dtype)
    # print(data.size)
    # print(data.empty)
    # print(data.ndim)
