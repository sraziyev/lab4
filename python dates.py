from datetime import date, timedelta
back = date.today() - timedelta(5)
print('Today:', date.today())
print('Five days ago:', back)

yesterday=date.today()-timedelta(1)
print('Yesterday:', yesterday)
tomorrow=date.today()+timedelta(1)
print('Tomorrow:', tomorrow)

from datetime import datetime
now=datetime.now()
print("Time now: ",now)
nownoms=now.replace(microsecond=0)
print("Time now without ms:",nownoms)


from datetime import datetime

def inputdate(prompt):
    date_str = input(prompt)
    return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

date1 = inputdate("Input first date in YYYY-MM-DD HH:MM:SS format: ")
date2 = inputdate("Input second date in YYYY-MM-DD HH:MM:SS format: ")

diff = date2 - date1
diffins = diff.total_seconds()

print(f"Difference between {date2} and {date1} is {diffins} s.")
