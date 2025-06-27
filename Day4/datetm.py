import datetime

my_dt=datetime.date(2024, 10, 28)
print(my_dt)

my_time = datetime.time(14, 30, 45, 123456)
print(my_time)

my_dtm = datetime.datetime(2024, 7, 24, 9, 15, 0)
print(my_dtm)

now = datetime.datetime.now()

formatted_dtm = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_dtm)

future_date = now + datetime.timedelta(days=2)
print(future_date)

past_time = now - datetime.timedelta(hours=3)
print(past_time)

differ = future_date - past_time
print(differ)

sl_offset = datetime.timezone(datetime.timedelta(hours=5,minutes=30))
now_sl = datetime.datetime.now(sl_offset)
print(now_sl)