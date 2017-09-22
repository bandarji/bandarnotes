# Datetimes

```python
import datetime
dir(datetime)
gvr = datetime.date(1956, 1, 31) # Guido van Rossum's birthdate
print(gvr)
print(gvr.year, gvr.month, gvr.day)
```

```python
mill = datetime.date(2000, 1, 1) # not the start of the century, but okay
dt = datetime.timedelta(100)
print(mill + dt)
```

```python
print(gvr.strftime("%A, %B %d, %Y"))
message = "GVR was born on {:%A, %B %d, %Y}."
print(message.format(gvr))
```

```python
launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)
print(launch_date, launch_time, launch_datetime)
print(launch_time.hour, launch_time.minute, launch_time.second)
print(launch_datetime.year, launch_datetime.month,
      launch_datetime.day, launch_datetime.hour,
      launch_datetime.minute, launch_datetime.second)
```

```python
now = datetime.datetime.today()
print(now)
print(now.microsecond)
```

```python
moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)
print(type(moon_landing_datetime)) # <class 'datetime.datetime'>
```
