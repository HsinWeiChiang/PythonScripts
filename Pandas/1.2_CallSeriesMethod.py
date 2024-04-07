import pandas as pd
import numpy as np

s_attr_methods = set(dir(pd.Series))
df_attr_methods = set(dir(pd.DataFrame))

###列出Series的屬性與方法總數
#print(len(s_attr_methods))

###列出DataFrame的屬性與方法總數
#print(len(df_attr_methods))

###列出df與series共有的屬性與方法
#print(len(df_attr_methods & s_attr_methods))

movies =  pd.read_csv('C:/Users/Wally/PythonScripts/Pandas/F1369_Code/data/movie.csv')

director = movies['director_name']
fb_likes = movies['actor_1_facebook_likes']
#print(director.dtype)
#print(fb_likes.dtype)

#print(director.head())
#print(director.sample(n=5, random_state=42))
#print(fb_likes.head())

###計算資料出現次數, value)counts()傳回的一樣是Series, 是以 "資料"當作索引, 個別資料出現的次數作為值

#print(director.value_counts())

#print(fb_likes.value_counts())










