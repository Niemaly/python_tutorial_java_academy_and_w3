import datetime

d = datetime.datetime(1988, 3, 24)
print(d)
print(d.strftime("%B"))


now = datetime.datetime.now()
print(now.microsecond)