import datetime
import sys
M,D = sys.stdin.readline().split()
str_datetime = '2007' +'-'+ M + '-' + D
format = '%Y-%m-%d'
dt_datetime = datetime.datetime.strptime(str_datetime,format)
print(dt_datetime.strftime('%a').upper())