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

print('mean =' + str(stats_mean(data)))
print('median = ' +  str(stats_median(data)))
print('mode ='+ str(stats_mode(data)))
print('Standard_deviation ='+ str(stats_std(data)))


