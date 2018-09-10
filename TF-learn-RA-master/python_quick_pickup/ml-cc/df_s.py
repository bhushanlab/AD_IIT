import numpy as np
import pandas as pd

def create_dataframe():
    # pd.DataFrame(data, index, columns, dtype, copy)
    # df = pd.DataFrame()
    data = np.arange(5)
    df = pd.DataFrame(data)
    df.columns = ["column A"]
    print (df)

    # using list to create the dataframe
    data = [[1,2,3],[4,5,6],[7,8,9]]
    """[[column 1, column 2, column 3],[column 1, column 2, column 3],[column 1, column 2, column 3]]"""
    df = pd.DataFrame(data,columns = ["This","That","Those"]) # this mirrors what we have above, column 1, column 2, column 3
    print (df)

    # create the dataframe via dict
    data = {"A": [1,2,3], "B" : [3,2,1], "C" : [8,9,10]}
    df = pd.DataFrame(data, index = [90,91,92])
    print (df)

    # create df from list of dictionarys
    data = [{'a':1, 'b':2},{'a':5, 'b':10, 'c':20}]
    """basically what this does, is that the keys in the dict is the column names, and the values is values"""
    df = pd.DataFrame(data)
    print (df) # for the 'c' since dict 1 int the list is missing the c value, thus, it is filled with NaN

    data = [{'a':1,'b':2,'c':3},{'a':2, 'b':3},{'a':312,'b':34,'c':912}]
    df = pd.DataFrame(data, index=np.arange(3))
    df2 = pd.DataFrame(data,index=np.arange(3),columns=['a','b','c','d'])
    # when creating the df, you can have more columns, however i tested, it is not possible for me to have more rows than provided
    print(df);print(df2)

    # create dataframe via series
    data = {'one':pd.Series([1,2,3],index=np.arange(3)), 'two':pd.Series([1,2,3,4],index=np.arange(4))}
    df = pd.DataFrame(data)
    print(df)

    # access df via columns
    print(df['one'])

    # add columns into existing df
    df['three'] = pd.Series([19,20,12])
    print (df)

    df['four'] = df['one'] + df['two']
    print (df) # generate the new column that is the sum of column one and two

    """column deletion"""
    d = {"one":pd.Series([1,2,3], index=["A","B","C"]), 'two':pd.Series([1,2,3,4], index=["A","B","C","D"]), 'three':pd.Series([10,20,30],index=['A','B','C'])}
    df = pd.DataFrame(d)
    print (df)
    # now we can delete a column
    del df['one']
    print (df)
    print(df.pop('two'))
    print (df)

    # row selection, addition, and deletion
    d = {"one":pd.Series([1,2,3], index=["A","B","C"]), 'two':pd.Series([1,2,3,4], index=["A","B","C","D"]), 'three':pd.Series([10,20,30],index=['A','B','C'])}
    df = pd.DataFrame(d)
    print(df.loc['D']) # print the D row
    # select by integer location
    print (df.iloc[0]) # print the first row
    # slice rows
    print (df[0:2])
    
    # add more rows
    df_temp = d = {"one": pd.Series([1, 2, 3], index=["E", "F", "G"]), 'two': pd.Series(
        [1, 2, 3, 4], index=["E", "F", "G", "H"]), 'three': pd.Series([10, 20, 30], index=['E', 'F', 'G'])}
    df = df.append(df_temp,ignore_index=True)
    print (df)

    # delete rows
    df = df.drop(0);df = df.drop(1)
    print (df)



def create_series1():
    data = np.array(['a', 'b', 'c', 'd'])
    s = pd.Series(data)
    return s

def create_series2():
    data = np.array(["a", "b", "c", "d"])
    s = pd.Series(data, index=[99,100,101,102])
    return s

def dict_to_series():
    my_diction = {"haha":1, "lolo":2, "GGGG":3}
    s = pd.Series(my_diction)
    #print s
    return s

def dict_to_series2():
    my_diction = {"haha": 1, "lolo": 2, "GGGG": 3}
    s = pd.Series(my_diction, index=["haha", "lolo", "GGGG"])
    return s

def main():
    temp_series1 = create_series1()
    print (temp_series1)
    temp_series2 = create_series2()
    print (temp_series2)
    temp_series3 = dict_to_series()
    print(temp_series3)
    temp_series4 = dict_to_series2()
    print(temp_series4)
    create_dataframe()

if __name__ == "__main__":
    main()
