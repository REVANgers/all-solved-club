import datetime

t = datetime.datetime.now(datetime.timezone.utc)
pacific_time = t - datetime.timedelta(hours=7)
day = pacific_time.day

name = '-'.join(input().lower().split())
f = open(f"day{day}-{name}.py", 'w')
f.close()