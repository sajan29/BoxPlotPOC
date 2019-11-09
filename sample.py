import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

dataframe=pd.read_csv("./titanic/train.csv")

print("------------------Shape of Dataframe----------------------")
print(dataframe.shape) #Size of dataframe
print("----------------------------------------------------------")

print("------------------Head of Dataframe----------------------")
print(dataframe.head()) #Printing head of dataframe
print("----------------------------------------------------------")

print("------------------Description of Dataframe----------------------")
dataframe_desc=dataframe.describe()  #Description of dataframe

print(dataframe_desc) #Printing description of dataframe
print("----------------------------------------------------------")

print("------------------Datatypes of Dataframe----------------------")
print(dataframe.dtypes)
print("----------------------------------------------------------")

df_boxplot=dataframe[['Age','Fare']]

print("------------------Dataframe melt----------------------")

df_melt=pd.melt(df_boxplot)
print(df_melt)
print("----------------------------------------------------------")

sns.boxplot(x="variable", y="value", data=pd.melt(df_boxplot))

plt.show()


