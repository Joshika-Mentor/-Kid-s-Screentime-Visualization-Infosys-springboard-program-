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
df1 #slicing the column data

#to find number of rows and columns will use shape
df.shape

#check for missing values will use isnull and number of null values will use isnull().sum()
df.isnull().sum()

#check the duplicate
df.duplicated().sum()

#drop duplicates
df.drop_duplicates(inplace=True)

df.info() #info after dropping the duplicates

#replacing the null value with 0
df['Health_Impacts'] = df['Health_Impacts'].fillna(df['Health_Impacts'].mode()[0])
df.isnull().sum()

df['Gender']=df['Gender'].astype('category')
df['Urban_or_Rural'].astype('category')
print(df)# setting the as type