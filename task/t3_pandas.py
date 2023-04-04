import pandas as pd

path = pd.read_csv('/home/mujeeb/Desktop/internship/weather_project/task3_sir_hmmad/pandas_task/files/f2.csv')

event = path[' Events']
events = path[event.isin(['Rain', 'Snow', 'Rain-Snow'])]['PKT'].tolist()
print(events)