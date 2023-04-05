import pandas as pd

data = pd.read_csv('/home/mujeeb/Desktop/internship/weather_project/task3_sir_hmmad/pandas_task/files/f1.csv')

max_min_difference = data['Max TemperatureC'] - data['Min TemperatureC']
max_min_difference_inlist = max_min_difference.tolist()

print(max_min_difference_inlist)