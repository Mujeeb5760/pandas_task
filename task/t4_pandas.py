import pandas as pd

path = pd.read_csv('/home/mujeeb/Desktop/internship/weather_project/task3_sir_hmmad/pandas_task/files/f2.csv')

events = path[' Events']
thunderstorm_events = path[events.isin(['Thunderstorm'])]
events_date = pd.to_datetime(thunderstorm_events['PKT'])
week_day = events_date.dt.strftime('%A').tolist()
print(week_day)
