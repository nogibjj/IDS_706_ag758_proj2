import pandas as pd
data = pd.read_csv("forbes_2022_billionaires.csv")

def stats_mean(df):
    return df['age'].mean()
  

def stats_median(df):
    return df["age"].median()
  

def stats_mode(df):
    return df["age"].mode()
  

def stats_std(df):
    return df["age"].std()

print('mean =' + stats_mean(data))
print('median = ' +  stats_median(data))
print('mode ='+stats_mode(data))
print('Standard_deviation ='+ stats_std(data))


