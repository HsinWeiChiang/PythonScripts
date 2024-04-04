import pandas as pd
import numpy as np

movies = pd.read_csv('C:/Users/Wally/PythonScripts/Pandas/F1369_Code/data/movie.csv')

index = movies.index
columns = movies.columns
data = movies.values

#print(columns)
#print(data)
# print(type(index))
# print(type(columns))
# print(type(data))
# print(issubclass(index.__class__, pd.Index))
# print(issubclass(data.__class__, pd.Index))


# print(index.to_numpy())
# print(columns.to_numpy())
print(type(columns.to_numpy()))