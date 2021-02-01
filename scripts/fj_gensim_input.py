#!/usr/bin/env python3

# Load the modules used
import numpy as np
import pandas as pd
import re
import string
import nltk

# Set file names
raw_file = "../data/fake_job_postings.csv"
# raw_file = "../data/fj_small.csv"
corpus_file = ".gensim-cache/fj_processed.txt"
# corpus_file = ".gensim-cache/fj_small_processed.txt"

def fj_txt_only(df):
	"""
	Combine all the text fields, discard everything else except for the label
	Input: 
		Dataframe
	Returns:
		Processed dataframe
	"""
	
	df.fillna(" ", inplace = True)

	df['text'] = df['title'] + ' ' + df['location'] + ' ' + df['department'] + \
	' ' + df['company_profile'] + ' ' + df['description'] + ' ' + \
	df['requirements'] + ' ' + df['benefits'] + ' ' + df['employment_type'] + \
	' ' + df['required_education'] + ' ' + df['industry'] + ' ' + df['function'] 

	del df['title']
	del df['location']
	del df['department']
	del df['company_profile']
	del df['description']
	del df['requirements']
	del df['benefits']
	del df['employment_type']
	del df['required_experience']
	del df['required_education']
	del df['industry']
	del df['function']  
	
	del df['salary_range']
	del df['job_id']
	del df['telecommuting']
	del df['has_company_logo']
	del df['has_questions']

	return df

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

	print(df.describe())
	
	print ('NAs in data')
	print(df.isna().sum())

	return df


# Utilities to clean text

def remove_URL(text):
	url = re.compile(r"https?://\S+|www\.\S+")
	return url.sub(r"", text)

def remove_html(text):
	html = re.compile(r"<.*?>")
	return html.sub(r"", text)

def remove_emoji(string):
	emoji_pattern = re.compile(
		"["
		u"\U0001F600-\U0001F64F"  # emoticons
		u"\U0001F300-\U0001F5FF"  # symbols & pictographs
		u"\U0001F680-\U0001F6FF"  # transport & map symbols
		u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
		u"\U00002702-\U000027B0"
		u"\U000024C2-\U0001F251"
		"]+",
		flags=re.UNICODE,
	)
	return emoji_pattern.sub(r"", string)

def remove_punct(text):
	table = str.maketrans("", "", string.punctuation)
	return text.translate(table)


# more text cleaning - remove stopwords using NLTK
nltk.download('stopwords')
from nltk.corpus import stopwords
stop = set(stopwords.words("english"))

def remove_stopwords(text):
	text = [word.lower() for word in text.split() if word.lower() not in stop]

	return " ".join(text)


df = fj_load_df_from_csv("./", raw_file)
df = fj_txt_only(df)

# Actually clean the text
df['text'] = df['text'].map(lambda x: remove_URL(x))
df['text'] = df['text'].map(lambda x: remove_html(x))
df['text'] = df['text'].map(lambda x: remove_emoji(x))
df['text'] = df['text'].map(lambda x: remove_punct(x))
df['text'] = df["text"].map(remove_stopwords)

# remove the labels
df = df['text']

# save the processed file for future use by gensim
df.to_csv(corpus_file, header=False, index=False)
