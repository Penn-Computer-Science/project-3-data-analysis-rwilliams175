import pandas as pd
import seaborn as sns
import matplotlib.pyplot as pit

df = pd.read_csv('form_results.csv')
balanceData = pd.DataFrame(df)
print("-_"*20)
print("Head of the Dataframe")
print(balanceData.head())

print("-_"*20)
print("Tail of the Dataframe")
print(balanceData.tail())

print("-_"*20)
print("Summary of the Dataframe")
print(balanceData.info())

print("-_"*20)
print("Statistics of the Dataframe")
print(round(balanceData.describe()))
