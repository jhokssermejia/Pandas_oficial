import pandas as pd 

path = '2017_2019.csv'

Solar_data = pd.read_csv(path, encoding = 'latin1')

print(type(Solar_data))
print(Solar_data)