import pandas as pd
import numpy as np

movies =  pd.read_csv('C:/Users/Wally/PythonScripts/Pandas/F1369_Code/data/movie.csv')

#print(movies['director_name'])

#print(movies.director_name)

#以欄位名稱來選取資料
    #print(movies.loc[:, 'director_name'])

#以欄位"位置"來選取資料
    #print(movies.iloc[:, 1])
    
#查詢索引標籤
    #print(movies['director_name'].index)

#查詢資料型別
    #print(movies['director_name'].dtype)
   
###查詢資料筆數
#print(movies['director_name'].size)

###查詢原本所屬的欄位名稱
#print(movies['director_name'].name)

###透過type()來查看傳回的物件類型
#print(type(movies['director_name']))

###只顯示出現過的資料型別,無需顯示Series中每筆資料的型別
print(movies['director_name'].apply(type).unique())


