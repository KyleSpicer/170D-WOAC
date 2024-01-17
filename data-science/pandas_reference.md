# Pandas Quick Reference

All the content covered in this reference assumes pandas was imported with the alias "pd"

```python
import pandas as pd
```

## Load a Dataset as Dataframe

### CSV

```python
df = pd.read_csv('your_file.csv')
```
### Excel spreadsheet

```python
excel_df = pd.read_excel('your_file.xlsx')
```

### JSON

```python
json_df = pd.read_json('your_file.json')
```

### HTML Tables

Parse a webpage and load the first HTML Table as a Dataframe

*Note: you can iterate through the tables with indexing*

```python
html_tables = pd.read_html('http://your_web_page.com')
html_df = html_tables[0]  # Change index position to desired table

```

## Preview the Dataset

Once the dataframe is loaded, we can access the first 10 rows of the dataset using ```df.head()```  This can be useful to verify that the Dataframe loaded correctly.

## Dropping Missing Values

```python
# Drop every row with any missing values
df_cleaned = df.dropna()
```
By default, pandas interprets numpy nan (np.nan), None, and pandas NaT (pd.NaT - missing datetime or timedelta information) as NA values.

We can adjust the Dataframe's NA values when we load it to include additional values:

```python
# Reading the CSV file and treating 'NA' and 'NULL' as missing values
df = pd.read_csv('sample.csv', na_values=['NA', 'NULL'])
```
If our df looks like:

```python
     A    B     C
0  1.0  5.0   'NULL'
1  2.0  NaN   Dog
2  'NA'  3.0   Cat
3  4.0  8.0   Fish
```

then df.dropna() reduces the dataframe to:

```python
     A    B     C
3  4.0  8.0   Fish
```
Since rows 0, 1, and 2 all had different NA values ('NULL' and 'NA' being custom for this particular Dataframe.)

Suppose we don't care about missing values in rows 'A' or 'C' and only want to dropna() if the missing value is in row 'B':

```python
# Drop rows where column 'B' has NA
df_no_na_in_B = df.dropna(subset=['B'])
```
Leaving us with:
```python
     A    B     C
0  1.0  5.0   'NULL'
2  'NA'  3.0   Cat
3  4.0  8.0   Fish
``` 

## Filtering Rows

Using a simple Dataframe:

```python
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles']
}
df = pd.DataFrame(data)

```

```python
      Name  Age         City
0    Alice   25     New York
1      Bob   30  Los Angeles
2  Charlie   35     New York
3    David   40      Chicago
4      Eva   45  Los Angeles
```

We can filter the Dataframe to only include rows with match criteria:

```python
# Filter rows where age is greater than 30
filtered_df = df[df['Age'] > 30]
```

```python
      Name  Age         City
2  Charlie   35     New York
3    David   40      Chicago
4      Eva   45  Los Angeles
```
## Accessing Columns

We can access a specific columns using their column label as a "key" and accessing it the same way we would access a value in a python dictionary:

Using our earlier Dataframe:

```python
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles']
}
df = pd.DataFrame(data)

```

```python
      Name  Age         City
0    Alice   25     New York
1      Bob   30  Los Angeles
2  Charlie   35     New York
3    David   40      Chicago
4      Eva   45  Los Angeles
```
If we want to save the 'Name' column:

*Note: this does not create a new Dataframe - but rather a different object entirely.  df column objects have their own methods associated with them and cannot be interchangeably treated as Dataframes.*

```python
names = df['Name']
```

```python
Name column:
0      Alice
1        Bob
2    Charlie
3      David
4        Eva

```

### Sorting

Dataframes can be sorted using the sort_values() function against a column:

If we don't want the default behavior of the sort function (alphabetical for strings/lowest -> highest for numbers) we can sort with a lambda function.  Here's an example on our above dataframe sorting by the length of the values in the City column:

```python
sorted_df = df.sort_values(by='City', key=lambda x: x.str.len())

```
Gives us:
```python
      Name  Age         City
3    David   40      Chicago
0    Alice   25     New York
2  Charlie   35     New York
1      Bob   30  Los Angeles
4      Eva   45  Los Angeles

```

### Descriptive Statistics

For columns with Numerical values, such as the Age column above, ew can get basically statistical data using the .describe() method of the column object:

```python
age_stats = df['Age'].describe()
```

Produces:
```python
count     5.00
mean     35.00
std       7.91
min      25.00
25%      30.00
50%      35.00
75%      40.00
max      45.00
Name: Age, dtype: float64
```

### Other numerical column methods:

Here are some other methods which can be applied to numerical columns in pandas.  This is not an exhaustive list:

* .sum(): Calculates the sum of the values in the column.

* .mean(): Computes the mean (average) of the values in the column.

* .median(): Finds the median (middle value) of the values in the column.

* .mode(): Identifies the mode(s) of the column, which is the value(s) that appear most frequently.

* .min(): Determines the minimum value in the column.

* .max(): Finds the maximum value in the column.

* .std(): Calculates the standard deviation of the column, a measure of the amount of variation or dispersion of the set of values.

* .var(): Computes the variance of the column, which is a measure of the dispersion similar to the standard deviation, but more prone to outliers.

* .quantile(q): Returns the q-th quantile of the column values, where q is a number between 0 and 1. For example, 0.25 would give the 25th percentile.

* .count(): Counts the number of non-NA/null values in the column.

* .corr(other): Calculates the correlation between two columns.

* .abs(): Returns the absolute value of each element in the column.

* .round(decimals): Rounds each value in the column to a specified number of decimal places.

* .cumsum(): Computes the cumulative sum of the column values, returning a series of the same size with the cumulative sum.

* .cumprod(): Calculates the cumulative product of the column values.

* .diff(periods): Computes the difference of a column element compared with another element in the column (default is the element in the previous row).

* .pct_change(): Computes the percentage change between the current and a prior element.