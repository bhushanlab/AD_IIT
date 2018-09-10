import numpy as np
import pandas as pd
# import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import pylab
# import openpyxl as oxl

def openExcelSheet(path, sheet_name): # convert the excelsheet to df
    dataframe_excel = pd.read_excel(path, sheet_name)
    #print (dataframe_excel)  
    #print ("------------clincal diagnosis------------")
    #print (dataframe_excel["dcfdx"])  
    return dataframe_excel

def analysis_1(df): # plot out the chnages
    tmp_df = df[df.columns[5:89]]
    print (tmp_df)
    plt.figure(); tmp_df.plot()
    plt.show()

def analysis_2(df): # plot the changes one column by another
    """
    display the change based on each visit of cataglorized by columns, each values
    is a row in that column
    """
    all_the_column_names = df.columns.get_values()
    all_the_column_names = all_the_column_names.tolist()
    for i in range(0, df.shape[1]):
        print (df[df.columns[i]])
        temp_df = df[df.columns[i]]
        plt.grid();plt.figure(); temp_df.plot(); plt.title(all_the_column_names[i])
    plt.show()

def analysis_2_1(df, df1 = None):
    all_the_column_names = df.columns.get_values()
    all_the_column_names = all_the_column_names.tolist()

    for i in range(0, df.shape[1]):
        temp_series = df[df.columns[i]][2:5]
        # print (temp_series)
        if df1.empty != True:
            temp_series1 = df1[df1.columns[i]][2:5]
            # print("================df1")
            # print(temp_series1)
            temp_series1.plot()

        plt.grid()
        plt.figure()
        temp_series.plot()
        plt.title(all_the_column_names[i])
    plt.show()

def analysis_3(df):
    temp_df = df.copy()
    column_names = list(temp_df.columns.values)
    monitor_dict = {}
    for i in range(4,89):
        change = float(temp_df.iloc[-1,i]) - float(temp_df.iloc[0,i])
        # need to deal with NaN
        # print(change)
        monitor_dict[i] = change
    return monitor_dict


def dataframe_compare_based_fuyearO(dataframe):
    amount_of_rows = dataframe.shape[0] #amount of rows is acquired by df.shape[0], df.shape[1] = amount of columns
    final_diff = pd.DataFrame(columns = dataframe.columns[5:89].values.tolist())
    for i in range(1, amount_of_rows):
        prev = i-1
        print(prev)
        diff_temp = dataframe.iloc[i][5:89] - dataframe.iloc[prev][5:89]
        # it is the later year - the year before e.g = 2nd year - 1st year
        final_diff = final_diff.append(diff_temp, ignore_index=True)
        print(diff_temp)
    return final_diff



def main():
    splitor =  "+++++++++++++++++++++++++++++++++++++++"
    writer_excel = pd.ExcelWriter('output.xlsx')
    path = '/Users/haominshi/Desktop/al_data/individual.xlsx'

    df_1 = openExcelSheet(
        path,sheet_name="Sheet1")
    df_2 = openExcelSheet(
        path, sheet_name="Sheet2")
    
    # first, focus on the df1, find out the change of each value based on the time
    # visit to the clinic
    # Data = Data frame 1, for a subj without alzheimer
    # fu_year = 0~7, indicate the visit times
    df_1_diff_based_on_year = dataframe_compare_based_fuyearO(df_1)
    df_1_diff_based_on_year.to_excel(writer_excel, 'O_DF 1 diff by year')

    # do the same thing for the 2nd sbj, that has the alzheimer
    df_2_diff_based_on_year = dataframe_compare_based_fuyearO(df_2)
    df_2_diff_based_on_year.to_excel(writer_excel, 'I_DF 2 diff by year')
    #analysis_2(df_2_diff_based_on_year)
    analysis_2_1(df_2_diff_based_on_year , df_1_diff_based_on_year) #detailed look at status changing from (dcfdx = 0,2,4)




if __name__ == "__main__":
    main()
