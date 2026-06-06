import pandas as pd

data = {

    "employee_id": [101,102,103],

    "name": [
        "Rahul",
        "Priya",
        "Amit"
    ],

    "salary": [
        75000,
        85000,
        65000
    ]
}
df=pd.DataFrame(data)
print(df)

df1=pd.read_csv("employee.csv")
print(df1)

#top few records
print(df1.head())

print(df1.tail())

print(df1.dtypes)

print(df1.info)

print(df1.describe())

print(df1[['name','salary']])



print(df1.iloc[2,2])

print(df1.isnull())