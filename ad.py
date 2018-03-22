import datetime
from pandas import DataFrame

DATE_FORMAT = '%d/%m/%Y'
DATE_OUT = '%d/%m'

start_date = '05/03/2018'
cur = datetime.datetime.strptime(start_date, DATE_FORMAT)
sprint = 0
table = []
while cur.month <= 7:
    next_cur = cur + datetime.timedelta(days = 7)
    row = [sprint, cur.strftime(DATE_OUT), next_cur.strftime(DATE_OUT)]
    table.append(row)
    cur = next_cur
    sprint += 1

dt = DataFrame(table)
dt.to_csv('cronograma.csv', index=False)
