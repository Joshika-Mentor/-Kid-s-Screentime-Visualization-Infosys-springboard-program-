# Here first we are importing Pandas library and connecting the drive for the data set
import pandas as pd
df="screen_time.csv"
df=pd.read_csv("/content/drive/MyDrive/Dateset/screen_time.csv")
df.head(10) #getting the first 10 rows of data
df.tail(10) #getting the Last 10 rows of data
df.describe() # getting the general describetion of the table

df1=df[["Primary_Device", "Age"]]
df1 #checking two columns in the table 

df1=df[["Primary_Device", "Age"]][1:10:1]
df1# slicing the data
