import numpy as np
import pandas as pd
import json

file_n = '../Files/name.csv'
file_c = '../Files/company.csv'

name = pd.read_csv(file_n)
cname = pd.read_csv(file_c)
name = name['name'].to_list()
cname = cname['Company'].to_list()
size = 500

name = np.random.choice(name, size)
cname = np.random.choice(cname, size)
email = [nam.lower().replace(' ', '') + '@' + cam.lower().replace(' ', '') + '.com' for nam, cam in zip(name, cname)]
phone = list(map(str, np.random.randint(6263474292, 9988776655, size)))

ra = list(range(20, 30)) + list(range(78, 90)) + list(range(155, 195)) + list(range(250, 309)) + list(
    range(355, 375)) + list(range(435, 445))
data = []
i = 0
for n, c, e, p in zip(name, cname, email, phone):
    if i in ra:
        d = {
            'name': n,
            'company': c,
            'phone': p
        }
    else:
        d = {
            'name': n,
            'email': e,
            'company': c,
            'phone': p
        }
    data.append(d)
    i += 1

print(data)
data = json.dumps(data)
with open('../Files/UserData.json', 'w') as file:
    file.writelines(data)
