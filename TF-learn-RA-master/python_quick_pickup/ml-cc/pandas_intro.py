import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series(np.arange(0,10,dtype=float))
print(s)

dates = pd.date_range('20130101', periods=10)
print (dates)

# construct the dataFrame, with index from dates and column, with ABCDE
df = pd.DataFrame(np.random.randn(10,5)*10, index = dates, columns=list('ABCDE'))
print (df)

df2 = pd.DataFrame({
    "A" : list("HAPPY"),
    "B" : [1,3,4,5,6],
    "C" : pd.date_range(start="20180522",periods=5)
})

print(df2);print(df2.dtypes)
print(df.A);print(df["A"])

print(df.A[:3])
print(df[:3][:1])
print(df.loc[dates[0]])

print(df.iloc[3:5,0:2]);print(df.iloc[0,2])

print(df > 0);print(df.A > 0)
df3 = df[df>0]
print(df3);print(df)

df3 = df.copy()
df3['F'] = pd.date_range('20180522',periods=10)
print(df3)
df3 = df3.drop(columns=['F'])
print(df3)

# some series
s1 = pd.Series([1,2,3,4,5,6,7,8,9,10],index=pd.date_range(start="20130101",periods=10))
print(s1)
df3["F"] = s1
print(df3)

print(df3.at[dates[0],'A'])
print(df3.iat[0,0])
df3.loc[:,'D'] = np.arange(0,10)
print(df3)
df3.loc[:,"D"] = np.array([5]*len(df3))
print(df3)

print(np.array([5]*3))

pieces = [df3[:3],df3[3:]]
print(pieces[0]); print(pieces[1])
df4 = pd.concat(pieces)
print (df4)

df_grade = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6], "raw_grade": 
                  list('abbaae')})
df_grade["grade"] = df_grade["raw_grade"].astype("category")
print(df_grade["grade"])
df_grade["grade"].cat.categories = ["very good", "good", "very bad"]
df_grade["grade"] = df_grade["grade"].cat.set_categories(
    ["very bad", "bad", "medium", "good", "very good"])
print(df_grade)