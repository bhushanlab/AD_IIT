import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# import openpyxl as oxl
import SingleFocus_1 as sf1
import Dropper as dropper
import time as t
# experiment
import missingno as msno
# from pylab import rcParams


'''
the purpose of this file is to scan the csv
then group the subject based on their ID number
create a list of df that each df is one patient
with 2 group:
    1. was diagnosed
    2. was not diagnosed
'''
def grouping(df):
    """
    create a list of dataframes, each element of the list contains a dataframe
    that is grouped by ID
    """
    # convert the values from the projid to a list
    projid_list = df.projid.unique()
    projid_list = projid_list.tolist() #list acquired this is a unique list of ID

    list_of_patients = []
    counter_start_df_row = 0 # used for slicing the df, first
    counter_end_df_row   = 0 # used for slicing the df, last
    counter_flag_start   = 0 # "for loop" start index for df spliting based on unique ID
    df = df.reset_index(drop = True) # df reindexed

    # messy
    for p_id in projid_list: # loop through the unique id list
        for df_index in range(counter_flag_start, df.shape[0]): 
            if df.iloc[df_index]['projid'] == p_id:
                counter_end_df_row += 1
            elif df.iloc[df_index]['projid'] != p_id:
                break
        # print("List appended ===>>> " + str(p_id))
        list_of_patients.append(df[counter_start_df_row: counter_end_df_row])
        counter_start_df_row = counter_end_df_row
        counter_flag_start = counter_end_df_row

    # print (list_of_patients) #CHECKED
    return list_of_patients # a list of df, that each element of the list is one patient

def patient_analysis(list_of_patient_diagnosed, list_of_patient_not_diagnosed = None):
    """
    list = [df1, df2, df3 ...]
    Analysis DF on a patient based scale
    """
    temp_list_p_diagnosed = list_of_patient_diagnosed.copy()
    # example of heatMap =  SNS https://stackoverflow.com/questions/12286607/python-making-heatmap-from-dataframe
    # heatmap matplot = https://stackoverflow.com/questions/12286607/python-making-heatmap-from-dataframe
    """
    plan:
        . . .
    """
    interesting_attr = ['chlstrl',
                        'crn', 'gfr_mdrs', 'glucose',
                        'hba1c', 'hdlchlstrl',
                        'hdlratio',
                        'hemacrit',
                        'hemoglbn',
                        'ldlchlstrl',
                        'mch',
                        'mchc',
                        'mcv',
                        'platelet', 'rbc', 'dcfdx'] # some interesting attr
    # for patient in temp_list_p_diagnosed:
        
        

    # need to finish this tomorrow


def sort_patient(list_of_patient):
    """
    split the patient based of if the patient was diagnosed or not
    """
    list_of_patient_diagnosed = []      # with alzheimer
    list_of_patient_not_diagnosed = []  # without alzheimer
    diagonosed_flag = False

    for patient in list_of_patient:
        dcfdx_check_list = patient['dcfdx'].tolist()
        for dcfdx_element in dcfdx_check_list:
            if dcfdx_element >= 4: # >= 4 means diagnoised
                diagonosed_flag = True
                break
        if (diagonosed_flag) == True:
            list_of_patient_diagnosed.append(patient)
            diagonosed_flag = False
        else:
            list_of_patient_not_diagnosed.append(patient)
    
    return list_of_patient_diagnosed, list_of_patient_not_diagnosed

def output_table_xlsx(df, output_filename): # dataframe, string
    """
    helper function to output df back to xlsx
    to get a better view of all the columns
    """
    writer_excel = pd.ExcelWriter(output_filename + ".xlsx")
    df.to_excel(writer_excel, 'Sheet1')
    print ("file created")

def sort_cases(cleaned_df): # based on the parameter DF, create 2 DF, based on
                            # the value of "dcfdx". smaller or larger than 4
    dcfdx_split_lvl = 4     # diagnosed flag >= 4 diagnosed, smaller than 4 is not

    cleaned_df = cleaned_df.reset_index(drop = True)  # df reindexed
    # need to create 2 empty df
    df_column_name_list = list(cleaned_df)
    tot_rows = cleaned_df.shape[0]

    new_diagnosed_df_by_case = pd.DataFrame(columns=df_column_name_list) #create a new empty df
    new_not_diagnosed_df_by_case = pd.DataFrame(columns=df_column_name_list)

    for row in range(0, tot_rows):  # loop through all the rows in the DF
        if cleaned_df.iloc[row]['dcfdx'] >= dcfdx_split_lvl:
            # get the df row that is larger than 4
            new_diagnosed_df_by_case = new_diagnosed_df_by_case.append(cleaned_df.iloc[row], ignore_index= True)
        elif cleaned_df.iloc[row]['dcfdx'] < dcfdx_split_lvl:
            # get the df row that is smaller than 4
            new_not_diagnosed_df_by_case = new_not_diagnosed_df_by_case.append(cleaned_df.iloc[row], ignore_index= True)
        else:
            continue
    
    return new_diagnosed_df_by_case, new_not_diagnosed_df_by_case

# newly added code for doing some differnet kinkd of sort... 
# based on the parameter DF, create 2 DF, based on
def sort_cases_for_other_stages(cleaned_df):
                            # the value of "dcfdx". smaller or larger than 4
    dcfdx_split_lvl_1 = 1     # diagnosed flag >= 4 diagnosed, smaller than 4 is not
    dcfdx_split_lvl_2 = 2
    cleaned_df = cleaned_df.reset_index(drop=True)  # df reindexed
    # need to create 2 empty df
    df_column_name_list = list(cleaned_df)
    tot_rows = cleaned_df.shape[0]

    new_diagnosed_df_by_case = pd.DataFrame(
        columns=df_column_name_list)  # create a new empty df
    new_not_diagnosed_df_by_case = pd.DataFrame(columns=df_column_name_list)

    for row in range(0, tot_rows):  # loop through all the rows in the DF
        if cleaned_df.iloc[row]['dcfdx'] >= dcfdx_split_lvl_2:
            # get the df row that is larger than 4
            new_diagnosed_df_by_case = new_diagnosed_df_by_case.append(
                cleaned_df.iloc[row], ignore_index=True)
        elif cleaned_df.iloc[row]['dcfdx'] == dcfdx_split_lvl_1:
            # get the df row that is smaller than 4
            new_not_diagnosed_df_by_case = new_not_diagnosed_df_by_case.append(
                cleaned_df.iloc[row], ignore_index=True)
        else:
            continue
    return new_not_diagnosed_df_by_case, new_diagnosed_df_by_case
#---------------------------------------------------------
# the newly implemented ploting is all in the notebook file, I will just be adding function and algorithm on this py file.
#---------------------------------------------------------
df_dcfdx_stage_1, df_dcfdx_stage_4 = \
    sort_cases_for_other_stages(data_set_cleaned)
print("sorting completed")

def main():
    path = '/Users/haominshi/Desktop/al_data/dataset_576_long.xlsx'
    path_test = '/Users/haominshi/Desktop/al_data/dataset_testing_short.xlsx'
    print ("Processing...")
    timer_1 = t.time()
    # =============================== Change path here
    data_set_everything = sf1.openExcelSheet(path, sheet_name="Sheet0")
    #data_set_everything = sf1.openExcelSheet(path_test, "Sheet1")
    # ==========================================================================
    
    # ==========================================================================
    timer_1 = t.time() - timer_1
    print (timer_1)
    print (data_set_everything.shape)
    print ("DF loaded")
    # file transfered to DF
    timer_1 = t.time()
    # ==========================================================================
    data_set_everything = dropper.drop_none_important_features(data_set_everything)
    # drop none important features
    data_set_everything = dropper.clean_history(data_set_everything)
    # ==========================================================================
    timer_1 = t.time() - timer_1
    print(timer_1)
    print(data_set_everything.shape)
    data_set_cleaned = data_set_everything.copy() 
    # the cleaned dataset's index is not droped
    print("DF cleaned") 
    # ==========================================================================
    print("DF grouping")
    timer_1 = t.time()
    # list_of_patient = list of df based on each patient, each element of the list
    # is a patient, and in that patient, we have the DF for each of their visit
    list_of_patient = grouping(data_set_cleaned)
    timer_1 = t.time() - timer_1
    print(timer_1)
    print("DF grouped dtype = list, total patient count is: " \
    + str(len(list_of_patient)))
    # ==========================================================================
    print("DF sorting")
    timer_1 = t.time()

    # 2 very important asset, all the manipulation use these 2
    list_of_patient_diagnosed, list_of_patient_not_diagnosed = \
    sort_patient(list_of_patient) # return 2 list of patient, split by if diagnosed
                                  # or not diagnosed
    timer_1 = t.time() - timer_1
    print(timer_1)
    print("2 list generated, diagnosed, and not diagnosed")
    print("Amount of patient diagnosed = " + str(len(list_of_patient_diagnosed)))
    print("Amount of patient not diagnosed = " + str(len(list_of_patient_not_diagnosed)))
    # ==========================================================================
    # print (list_of_patient_diagnosed)
    # output_table_xlsx(data_set_cleaned,"output_cleaned_dataSet")
    # from column [66:] is boolean value [1,0]
    patient_analysis(list_of_patient_diagnosed)

    #experiment new tools - this is added to JUPY
    msno.matrix(data_set_cleaned)
    sort_cases(data_set_cleaned)

    # 2 DF, one is diagnosed, one is not diagonesed
    df_diagnosed_df_by_case, df_not_diagnosed_df_by_case = sort_cases(data_set_cleaned)
    print("2 DF created, grouped by diagnosed and not diagnosed")

    # want to take a look at the difference between avg of df_diagnosed and not_diagnosed
    df_diagnosed_desc = df_diagnosed_df_by_case.describe()
    df_not_diagnosed_desc = df_not_diagnosed_df_by_case.describe()
    # now i think i am going to select the row that is the mean, and compare them


if __name__ == "__main__":
    main()
