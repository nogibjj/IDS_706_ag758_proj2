import pandas as pd
data = pd.read_csv("..csv")

def stats_mean(df):
    return df['age'].mean()
  

def stats_median(df):
    return df["age"].median()
  

def stats_mode(df):
    return df["age"].mode()
  

def stats_std(df):
    return df["age"].std()

print(stats_mean(data))
print(stats_median(data))
print(stats_mode(data))



