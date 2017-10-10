# CSV / Comma Separated Values

Python can easily work with this popular data format.


## Movie Data

```
Title,Year Released,Director
The Godfather,1972,Francis Ford Coppola
The Shawshank Redemption,1994,Frank Darabont
Citizen Kane,1941,Orson Welles
Gone With the Wind,1939,Victor Fleming
The Sound of Music,1965,Robert Wise
Spirited Away,2001,Hayao Miyazaki
"The Good, the Bad and the Ugly",1966,Sergio Leone
It's a Wonderful Life,1946,Frank Capra
Amadeus,1984,Milos Forman
The Lord of the Rings: The Return of the King,2003,Peter Jackson
Saving Private Ryan,1998,Steven Spilberg
Rear Window,,Alfred Hitchcock
Rocky,1976,John G. Avildsen
```

## Stock Market Data

[External Google Sheet link](https://goo.gl/3zaUlD)

Click File, Download as CSV...

## Read Stock Information

### Read and Display Content

```python
path = "/data/google_stock_data.csv"
file = open(path)
for line in file:
    print(line)
```

### Read and Store Content For Use

#### Without CSV Module

```python
lines = [line for line in open("/data/goog_data.csv")]
lines[0]
# 'Date,Open,High,Low,Close,Volume,Adj Close\n'
lines[1]
# '8/19/2014,585.002622,587.342658,584.002627,586.862643,978600,586.862643\n'
lines[0].strip() # remove newline character from end
lines[0].strip().split(',') # create list with comma as delimiter

dataset = [line.strip().split(',') for line in open("/data/goog_data.csv")]
```

Think about the movie data set. A movie title might include a comma. The
commands above would not split the data elements properly. The CSV
module takes that into account and processes appropriately.

#### With CSV Module

```python
import csv

path = "/data/goog_data.csv"
file = open(path, newline='') # Works for UNIX or DOS line endings
reader = csv.reader(file)

header = next(reader)
data = [row for row in reader]

print(header)
# ['Date', ..., 'Adj Close']
print(data[0])
# ['8/19/2014', ..., '586.862643']
```

```python
# Properly format inputs: strings vs floats vs dates vs integers
import csv
from datetime import datetime

path = "/data/goog_data.csv"
file = open(path, newline='') # Works for UNIX or DOS line endings
reader = csv.reader(file)

header = next(reader)
data = []
for row in reader:
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1]) # 'open' is a builtin function
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])
    data.append(date, open_price, high, low, close, volume, adj_close) 
```

#### Display Daily Stock Returns

Stock returns equals the percent change in price. Interesting stock return
intervals: daily, weekly, monthly, quarterly and annually.

```python
# working with data list from above
returns_path = "/data/goog_returns.csv"
file = open(returns_path, 'w')
writer = csv.writer(file)
writer.writerow(["Date", "Return"])

for i in range(len(data) - 1):
    todays_row = data[i]
    todays_date = todays_row[0].strftime('%m/%d/%Y')
    todays_price = todays_row[-1]
    yesterdays_row = data[i+1]
    yesterdays_price = yesterdays_row[-1]
    daily_return = (todays_price - yesterdays_price) / yesterdays_price
    writer.writerow([todays_date, daily_return])
```
