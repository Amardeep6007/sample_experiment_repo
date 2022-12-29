import pandas as pd 


data_file_path = '/config/workspace/mushroom.csv'
if __name__=='main':
    #df = pd.read_csv('E:/Mushroom_classification-main/Mushroom_classification-main/mushrooms.csv')
    df = pd.read_csv(data_file_path)
    print(df.head(5))