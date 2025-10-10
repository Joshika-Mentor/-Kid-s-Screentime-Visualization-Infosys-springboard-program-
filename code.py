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

#For chart plotting, impoting matplotlib and seaborn libraries
import matplotlib.pyplot as plt
import seaborn as sns

#plotting a histogram showing the distribution of screen time in hours
plt.figure(figsize=(8,5))
sns.histplot(df['Avg_Daily_Screen_Time_hr'],kde=True, color='lightblue')
plt.title('Distribution of screening time in Hours')
plt.xlabel('Avg_Daily_Screen_Time_hr')
plt.ylabel('Frequency')
plt.show()

#Countplot for Gender
sns.countplot(x='Gender', data= df)
plt.title('Gender')
plt.show()

#Countplot for Device type
sns.countplot(x='Primary_Device', data= df)
plt.title('Device type')
plt.show()

#Countplot for Location
sns.countplot(x='Urban_or_Rural', data= df)
plt.title('Location')
plt.show()

#violin plot for average screen time with respect to Gender
sns.violinplot(x='Gender', y='Avg_Daily_Screen_Time_hr', data=df, color='lightgreen')
plt.show()

#violin plot for average screen time with respect to Age
sns.violinplot(x='Age', y='Avg_Daily_Screen_Time_hr', data=df)
plt.show()

#box plot for average screen time with respect to Age
sns.boxplot(x='Age', y='Avg_Daily_Screen_Time_hr', data=df, 
hue='Age',palette='plasma', legend=True, )
plt.title('Box plot')
plt.figure(figsize=(8,5))
plt.show()

#box plot for average screen time with respect to Gender
sns.boxplot(x='Gender', y='Avg_Daily_Screen_Time_hr', 
data=df, hue='Gender',palette='plasma', legend=True, )
plt.title('Box plot')
plt.figure(figsize=(8,5))
plt.show()

# Histogram for distribution of screen time with respecct to average screen time
plt.figure(figsize=(8, 5))
sns.histplot(
    data=df,
    x='Avg_Daily_Screen_Time_hr',
    bins=20,           # Number of bins in the histogram
    kde=True,          # **Key: overlay the KDE curve**
    color='skyblue',
    edgecolor='black',
    linewidth=0.5
)
plt.title('Distribution of Screen Time')
plt.xlabel('Screen Time (Hours)')
plt.show()

# Histogram for distribution of screen time with respecct to Age
plt.figure(figsize=(10, 6))
sns.histplot(
    data=df,
    x='Age',
    bins=20,           # Number of bins in the histogram
    kde=True,          # **Key: overlay the KDE curve**
    color='skyblue',
    edgecolor='black',
    linewidth=0.5
)
plt.title('Distribution of Screen Time')
plt.xlabel('Screen Time (Hours)')
plt.show()

# KDE plot for distribution of screen time with respecct to average screen time
plt.figure(figsize=(8, 5))
sns.kdeplot(
    data=df,
    x='Avg_Daily_Screen_Time_hr',
    fill=True,      # **Key: fill the area under the curve**
    color='purple',
    alpha=0.6,
    linewidth=2
)
plt.title('Distribution of Age (KDE Plot)')
plt.show()

# KDE plot for distribution of screen time with respecct to Age
plt.figure(figsize=(8, 5))
sns.kdeplot(
    data=df,
    x='Age',
    fill=True,      # **Key: fill the area under the curve**
    color='purple',
    alpha=0.6,
    linewidth=2
)
plt.title('Distribution of Age (KDE Plot)')
plt.xlabel('Age (Years)')
plt.show()

# scatter plot Age Vs screen time
sns.scatterplot(
    data=df,
    x='Age',
    y='Avg_Daily_Screen_Time_hr'
)
plt.title('Age vs. screen time')
plt.show()

# Bar plot location Vs screen time differ by Gender
plt.figure(figsize=(10, 6))
sns.barplot(
    data=df,
    x='Urban_or_Rural',          # Primary grouping on the X-axis (Urban/Rural)
    y='Avg_Daily_Screen_Time_hr', # The numerical variable to average
    hue='Gender',                # Secondary grouping using color (Male/Female)
    palette='Set2',              # A different color palette
    errorbar='sd'                # Show standard deviation
)
plt.title('Average Screen Time: Urban vs. Rural by Gender')
plt.xlabel('Location Type')
plt.ylabel('Average Daily Screen Time (Hours)')
plt.legend(title='Gender')
plt.show()

# Bar plot Primary device Vs screen time differ by Gender
plt.figure(figsize=(10, 6))
sns.barplot(
    data=df,
    x='Primary_Device',          # Primary grouping on the X-axis (Urban/Rural)
    y='Avg_Daily_Screen_Time_hr', # The numerical variable to average
    hue='Gender',                # Secondary grouping using color (Male/Female)
    palette='Set2',              # A different color palette
    errorbar='sd'                # Show standard deviation
)
plt.title('Average Screen Time: Urban vs. Rural by Gender')
plt.xlabel('Location Type')
plt.ylabel('Average Daily Screen Time (Hours)')
plt.legend(title='Gender')
plt.show()