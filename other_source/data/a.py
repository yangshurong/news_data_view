import datetime
t='2019-04-29 00:00:00'
n='2018-05-31 00:00:00'
a=datetime.datetime.strptime(t, '%Y-%m-%d %H:%M:%S')
b=datetime.datetime.strptime(n, '%Y-%m-%d %H:%M:%S')
print(b-a)