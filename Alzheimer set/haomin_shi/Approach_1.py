# naive approach

import pandas as pd
import numpy as np
# import tensorflow as tf
from sklearn import tree
from sklearn.preprocessing import Imputer

def read_excel_data(path):
   dataframe_excel = pd.read_excel(path)
   return dataframe_excel

def split_data_set(datafame):
    """split data set to 3 pieces, training set, test set, and validation set"""
    """roughly ---> 50%, 25%, 25%"""
    dataframe_pieces = [datafame[0:12786],datafame[12786:19194],datafame[19194:]]
    """
    dataframe_pieces[0] = training 
    dataframe_pieces[1] = test
    dataframe_pieces[2] = validation
    """
    return dataframe_pieces

def acquire_labels(dataframe):
    """
    based on the info from the code sheet,
    The dcfdx is possibly the label - HS
    """
    pass

def drop_columns(dataframe):
    dataframe = dataframe.drop(columns=['projid','study','fu_year','scaled_to'])
    # projid - not important, same for study, fu_year is important -> but dont want to use it in this run
    # scaled_to - not important
    return dataframe
    # pass

def building_tree(dataframe): #for building the tree, use the pieces[0]
    dataframe_train_set = dataframe[0]
    features = []
    labels = dataframe_train_set["dcfdx"].tolist()
    print (labels)
    dataframe_train_set_features = dataframe_train_set.copy()
    dataframe_train_set_features = dataframe_train_set_features.drop(columns=['dcfdx'])
    # probably best to loop through the whole dataframe_training_set and drop the row with no dcfdx data
    # 05/22 - label nan need to drop row, feature nan can ignore data 

    for row in dataframe_train_set_features.iterrows():
        index, data = row
        features.append(data.tolist())
    print(features)

    # Create our imputer to replace missing values with the mean e.g.
    imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
    imp = imp.fit(features)
    imp_features = imp.transform(features)


    print("training . . .")
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features, labels)
    # have some problem, need to deal with NaN, thinking use neutural to replace them
    # feature NaN replace, not yet label
    return clf


def main():
    excel_file_path = "/Users/haominshi/Desktop/al_data/dataset_576_long.xlsx"
    datafame_1 = read_excel_data(excel_file_path)
    print(datafame_1)
    datafame_1_droped = drop_columns(datafame_1) # dropped some columns

    dataframe_pieces = split_data_set(datafame_1_droped)
    print(dataframe_pieces) # sets acquired
    model_tree = building_tree(dataframe_pieces)


if __name__ == "__main__":
    main()
