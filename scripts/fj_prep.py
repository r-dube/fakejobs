#!/usr/bin/env python3

"""
Data Preprocessing for Fake Jobs Data
Data source: https://www.kaggle.com/shivamb/real-or-fake-fake-jobposting-prediction
downloaded: 12/1/2020
"""

# Load the modules that are used in this script
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

# Some global variables to drive the script
in_dir = '/Users/rdube/Repos/fakejobs/data/'
in_data = 'fake_job_postings.csv'
out_dir = '/Users/rdube/Repos/fakejobs/data/'
small_data  ='fj_small.csv'
medium_data  ='fj_medium.csv'

def fj_label_stats(df):
    """
    """
    counts = np.bincount(df['fraudulent'])
    return counts

def fj_load_df_from_csv(dir, file):
    """
    Load dataframe from csv file
    Input:
        dir: directory for csv file
        file: csv file
    Returns:
        Pandas dataframe corresponding to processed and saved csv file
    """

    df = pd.read_csv(dir + file)

    counts = fj_label_stats(df)
    print ('Not fraudulent', counts[0], 'Fraudulent', counts[1])

    print(df.describe())

    print ('NAs in data')
    print(df.isna().sum())

    return df

def fj_split(df, split):
    """
    Input:
        Dataframe that has columns of covariates followed by a column of labels
        Percentage of records to be split out
    Returns:
        Two dataframes: df1, df2
    """

    print("df.shape", df.shape)

    df1, df2 = train_test_split(df, test_size=split, random_state=42)

    counts = fj_label_stats(df1)
    print ('trainval: ', 'Not fraudulent', counts[0], 'Fraudulent', counts[1])

    counts = fj_label_stats(df2)
    print ('test: ', 'Not fraudulent', counts[0], 'Fraudulent', counts[1])

    return df1, df2

def fj_preprocess1(df):
    pd.options.mode.use_inf_as_na = True

    df_p = pd.DataFrame()
    df_p['telecommuting'] = df['telecommuting']
    df_p['has_logo'] = df['has_company_logo']
    df_p['has_questions'] = df['has_questions']
    df_p['has_location'] = np.where(df['location'].notna() == True, 1, 0)
    df_p['has_department'] = np.where(df['department'].notna() == True, 1, 0)
    df_p['has_salary'] = np.where(df['salary_range'].notna() == True, 1, 0)
    df_p['has_profile'] = np.where(df['company_profile'].notna() == True, 1, 0)
    df_p['has_requirements'] = np.where(df['requirements'].notna() == True, 1, 0)
    df_p['has_benefits'] = np.where(df['benefits'].notna() == True, 1, 0)
    df_p['has_type'] = np.where(df['employment_type'].notna() == True, 1, 0)
    df_p['has_experience'] = np.where(df['required_experience'].notna() == True, 1, 0)
    df_p['has_education'] = np.where(df['required_education'].notna() == True, 1, 0)
    df_p['has_industry'] = np.where(df['industry'].notna() == True, 1, 0)
    df_p['has_function'] = np.where(df['function'].notna() == True, 1, 0)
    df_p['fraudulent'] = df['fraudulent']

    print(df_p.describe())

    return df_p

def fj_save(dir, file, df):
    df.to_csv(dir + file, index=False)
    return 

def fj_metrics(y_actual, y_pred):
    cm = confusion_matrix (y_actual, y_pred)
    print (cm)

    acc = accuracy_score (y_actual, y_pred)
    f1 = f1_score(y_actual, y_pred)
    print('Accuracy score: {:.4f}'.format(acc), 'F1 score: {:.4f}'.format(f1))

    return f1

def fj_logistic(df):
    """
    Input:
    Returns:
    """
    from sklearn.linear_model import LogisticRegression

    df_train, df_val = train_test_split(df, test_size=0.15, random_state=42)

    logreg = LogisticRegression(max_iter=100)
    logreg.fit(df_train.iloc[:,:-1], df_train.iloc[:,-1:])

    y_pred = logreg.predict(df_val.iloc[:,:-1])
    
    fj_metrics(df_val.iloc[:,-1:], y_pred)
    return


# def main():
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

df = fj_load_df_from_csv(in_dir, in_data)

# uncomment to run basic logistic regression model
# df = fj_preprocess1(df)
# fj_logistic(df)

df1, df2 = fj_split(df, 0.20)
fj_save(out_dir, medium_data, df2)
