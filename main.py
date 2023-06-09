import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Bengaluru_House_Data.csv')
df.drop(columns=['society', 'bath','balcony'], inplace=True)
print(df.isnull().sum())
