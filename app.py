import pandas as pd 
import logging as lg 

data_file_path = '/config/workspace/mushrooms.csv'
lg.INFO('We are inside the data frame')
df = pd.read_csv(data_file_path)
lg.INFO('counted the number of "?" marks in the stalk-root column')
print(f"stalk root column contains {df['stalk-root'][df['stalk-root']=='?'].count()} question marks '?' hence {df['stalk-root'][df['stalk-root']=='?'].count()} missing values in this column") #printing the number of question marks in the stalk root column
