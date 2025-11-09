
# ML_Time_Series

# Time Series Definitions
Stochastic Process - Random variable indexed by time

# Time series analysis

1. Define the problem: Is it a classification or regression problem? What are the inputs and outputs? What are the steps involved in solving the problem?
2. Data Exploration: This step involves visualizing the data to understand the trends and patterns. This helps in developing the intuition for building the machine learning model.
3. Preprocess the data: This step involves cleaning the data, dealing with missing values, and transforming the data so that it can be used by the machine learning algorithm. This step is crucial and includes feature engineering, scaling, normalization.
4. Decompose the time series: This step is useful in understanding the trend, seasonality, and noise in the data. This step is necessary for certain kinds of methods, but not with others.
5. Build models: Once the data is preprocessed, you can build models using traditional machine learning algorithms or time series specific algorithms.
6. Evaluate the models: This step includes comparing the performance of different models and choosing the best one. It involves assessing the performance of the machine learning model on unseen data. This helps in fine-tuning the model and making it ready for deployment.
7. Make predictions: This step involves using the final model to make predictions on new data.

# Common formating operations  

Complete list of formatting options that you can use both for parsing strings and printing datetime objects here: https://strftime.org/  

* Use the header option to tell read_csv() which row is the header
```
df = read_csv("data.csv", header=0)
```
* Use the index_col option to tell read_csv() which column to use as the index. The index is a special column that contains the labels for the rows
```
df = read_csv("data.csv", index_col="date")
df.head(4)
```
* Data type
```
df.dtypes
```
* Use the parse_dates option to tell read_csv()to parse the dates in the index.
```
df = read_csv("data.csv", parse_dates=["date"])
df.dtypes
```
* Use the date_parser option to tell read_csv() how to parse the dates.
The date_parser option takes a function that takes a string containing a date, and parses it into a datetime object. The ignoretz option tells the parse() function to ignore the timezone information in the string.
```
from dateutil.parser import parse
def parse_dates(date_str):
    return parse(date_str, ignoretz=True)
df = read_csv("data.csv", date_parser=parse_dates)
df.head()
```
* Create a time series as follows:
```
import pandas as pd
pd.date_range(start='2021-03-24', end='2021-09-01')
```
OR
```
pd.Series(pd.date_range("2021", freq="D", periods=3))
```
* Parsing to date or datetime objects from either string or separate columns:
```
import pandas as pd
df = pd.DataFrame({'year': [2021, 2022],
    'month': [3, 4],
    'day': [24, 25]}
)
ts1 = pd.to_datetime(df)
ts2 = pd.to_datetime('20210324', format='%Y%m%d')
```
* Rolling window for calculations like this:
```
s = pd.Series([1, 2, 3, 4, 5])
s.rolling(3).sum()
```
OR
```
import numpy as np 
rng = pd.date_range('2021-03-24', '2021-09-01', freq='D')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
```
* Index these time series datasets like any other pandas Series or DataFrame. ts[:2].index would give us:
```
DatetimeIndex(['2021-03-24', '2021-03-25'], dtype='datetime64[ns]', freq='D')
```
OR
```
ts['2021-03-28':'2021-03-30']
```
* Shift or lag the values in a time series back and forward in time using the shift method. This changes the alignment of the data:
```
ts.shift(1)[:5]
```
* Change the resolution of time series objects, for example like this:
```
ts.asfreq('M')
```
* Working with dates we’ll import them, batteries included:
```
from datetime import date
today = date.today()
other_date = date(2021, 3, 24)
```
* Datetime object (a timestamp) instead, we can do this as well:
```
from datetime import datetime
now = datetime.now()
```
* Create a datetime for a specific date and time as well:
```
some_date = datetime(2021, 5, 18, 15, 39, 0)
some_date.isoformat()
```
* Time differences using timedelta:
```
from datetime import timedelta 
year = timedelta(days=365)
year * 10
```
* Converting between different lengths of time like this:
```
def to_seconds(*args, **kwargs):
    return datetime.timedelta(*args, **kwargs).total_seconds()
```
* Parse string inputs to date and datetime types and output these objects as string:
```
from datetime import date
some_date = date.fromisoformat('2021-03-24')
```
OR
```
some_date = datetime.date(2021, 3, 24)
```
* Format the output with string format options, for example like this:
```
  some_date.strftime('%A %d. %B %Y')
```
* Read in a date or datetime object from a string, and we can use the same format options:
```
from datetime import datetime
dt = datetime.strptime('24/03/21 15:48', '%d/%m/%y %H:%M')
```





