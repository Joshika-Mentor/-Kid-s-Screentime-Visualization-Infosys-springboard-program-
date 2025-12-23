# Load The Raw Data Set File

from google.colab import files
uploaded = files.upload()
print(uploaded)

# Import the Python libraries and data file

import pandas as pd

df = pd.read_csv('/content/Indian_Kids_Screen_Time.csv')
df.head()

# Check the data from Bottom 
df.tail()

# Describe about the data sheet
df.describe()

# Count the data 
df.count()

# Shape of datasheet
df.shape

# Load the data sheet to Fimd only Age group
import pandas as pd

df = pd.read_csv('/content/Indian_Kids_Screen_Time.csv')
df1=df["Age"]
df1

# Sum the duplicate data from datasheet
df.duplicated().sum()

# Data of Primary Device from datasheet
df1=df["Primary_Device"]
df1

# Get Information about the data 
df.info()

print(df.isnull().sum())

df.drop_duplicates(inplace=True)

df.value_counts()


df.isnull()

print(df.isnull().sum().sum())

# check the not null value from data
df.notnull()



# We Start The Week 2 – Univariate & Bivariate Analysis

# Distributions Plot Of Screen Time 
import matplotlib.pyplot as plt
import seaborn as sns

plt.figsize=(10,6)
sns.histplot(df['Avg_Daily_Screen_Time_hr'], kde=True, color="skyblue")
plt.title("distribution of screen time in hours")
plt.show()

# Histograms & KDE plots for continuous variables
import seaborn as sns
import matplotlib.pyplot as plt

# Histogram for Screen Time
plt.figsize=(10,6)
sns.histplot(
    data=df,
    x='Avg_Daily_Screen_Time_hr',
    kde=False,
    bins=25,
    color='skyblue',
    edgecolor='black'
)
plt.title('Distribution of Screen Time')
plt.xlabel('Screen Time (hours per day)')
plt.ylabel('Number of Students')
plt.show()

# Kernal Density Estimate For the Age / KDE Plot for Age
plt.figsize=(10,6)
sns.kdeplot(
    data=df,
    x='Age',
    fill=True,
    color='red',
    linewidth=3
)
plt.title('Distribution of Age')
plt.xlabel('Age (years)')
plt.ylabel('Density')
plt.show()

# Countplots for categorical variables

# Countplot for Gender
plt.figsize=(10,6)
sns.countplot(
    data=df,
    x='Gender',
    palette='cool',
    edgecolor='black'
)
plt.title('Count of Students by Gender')
plt.xlabel('Gender')
plt.ylabel('Number of Students')
plt.show()

 # Countplot for Device Type
plt.figsize=(8,5)
sns.countplot(
    data=df,
    x='Primary_Device',
    palette='dark',
    edgecolor='black'
)
plt.title('Devices Used by Students')
plt.xlabel('Device Type')
plt.ylabel('Number of Students')
plt.show()

# # Countplot for Location
plt.figsize=(6,4)
sns.countplot(
    data=df,
    x='Urban_or_Rural',
    palette='muted',
    edgecolor='black'
)
plt.title('Count of Students by Location')
plt.xlabel('Location')
plt.ylabel('Number of Students')
plt.show()

# Boxplots & Violin Plots

# Create the boxplot
plt.figsize=(7,5)
sns.boxplot(
    data=df,
    x='Gender',
    y='Avg_Daily_Screen_Time_hr',
    palette='Set2',
)
plt.title('Screen Time by Gender')
plt.xlabel('Gender')
plt.ylabel('Screen Time (hours per day)')
plt.show()

# # right Now we change the size
plt.figsize=(8,5)
sns.violinplot(
    data=df,
    x='Age',
    y='Avg_Daily_Screen_Time_hr',
    palette='cool',
)
plt.title('Screen Time by Age Group')
plt.xlabel('Age')
plt.ylabel('Screen Time (hours per day)')
plt.show()

# Check The Columns Of Data
print(df.columns)

# We can Compare the both Graphical Representation in One Frame

plt.figsize=(8,5)
sns.boxplot(
    data=df,
    x='Age',
    y='Avg_Daily_Screen_Time_hr',
    hue='Gender',
    palette='muted'
)
plt.title('Screen Time by Age Group and Gender')
plt.xlabel('Age')
plt.ylabel('Screen Time (hours per day)')
plt.legend(title='Gender')
plt.show()

# Scatterplots
#  Scatterplot: Age vs Screen Time

plt.figsize=(8,6)
sns.scatterplot(
    data=df,
    x='Age',
    y='Avg_Daily_Screen_Time_hr',
    hue='Gender',
    palette='muted',)
plt.title('Scatterplot of Age vs Screen Time')
plt.xlabel('Age (years)')
plt.ylabel('Screen Time (hours per day)')
plt.show()

# We Start The Week 3 - Comparative Analysis

# Grouped barplots
import seaborn as sns
import matplotlib.pyplot as plt

plt.figsize=(8,5)
sns.barplot(
    data = df,
    x='Urban_or_Rural',
    y='Avg_Daily_Screen_Time_hr',
    hue='Gender',
    palette='Set2',
)
plt.title('Average Screen Time: Urban vs Rural by Gender')
plt.xlabel('Location (Urban or Rural)')
plt.ylabel('Average Screen Time (hours per day)')
plt.show()

# Load Again a data set from device to goolge Colab
import pandas as pd

df = pd.read_csv('/content/Indian_Kids_Screen_Time.csv')
display(df.head())

# FacetGrid (screen time by device × gender) 
import seaborn as sns
import matplotlib.pyplot as plt

g = sns.FacetGrid(
    data=df,
    col='Gender',
    height=5,
    aspect=1
)

g.map_dataframe(
    sns.barplot,
    x='Primary_Device',
    y='Avg_Daily_Screen_Time_hr',
    palette='Set2'
)

g.set_axis_labels("Primary Device", "Average Screen Time (hours/day)")
g.set_titles(col_template="{col_name}") # Each plot title = Gender
plt.subplots_adjust(top=0.8)
g.fig.suptitle("Screen Time by Primary Device and Gender")
plt.show()

# Facegried with seperate devide with gender 
g = sns.FacetGrid(df, col='Gender', row='Primary_Device', height=4, aspect=1.2)
g.map(sns.histplot, 'Avg_Daily_Screen_Time_hr', kde=True)
g.fig.suptitle('Distribution of Average Daily Screen Time by Primary Device and Gender', y=1.03)
g.set_axis_labels('Average Daily Screen Time (hours)', 'Frequency')
plt.tight_layout()
plt.show()

# Pairplot (relationships between numerical variables)

# We use The Age And Screen Time By  gender

import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")
# Create the pairplot
g = sns.pairplot(
    data=df,
    vars=['Age', 'Avg_Daily_Screen_Time_hr'],
    hue='Gender',
    palette='muted',
)
# Add a bold main title
g.fig.suptitle(
    "Relationship Between Age and Average Daily Screen Time by Gender",
    fontsize=14,
    fontweight='bold',
    y=1.03 # Corrected indentation
)
# Remove individual axis labels
for ax in g.axes.flatten():
    if ax is not None:
        ax.set_xlabel("")
        ax.set_ylabel("")

# Add overall x and y labels for the figure
g.fig.text(0.5, 0.0002, 'Age', ha='center', fontsize=12)
g.fig.text(0.0002, 0.5, 'Average Daily Screen Time', va='center', rotation='vertical', fontsize=12)

plt.figtext(
    0.5, 0.0002,  # Adjust y coordinate to move text to the bottom
    "This plot helps us visualize how screen time changes with age, separated by gender.",
    ha = 'center',
    fontsize=11,
    color='gray'
)
plt.tight_layout()

plt.show()

# Heatmap (Correlation between Screen Time , Age & Educational_to _Recreational_Ratio) 
import seaborn as sns
import matplotlib.pyplot as plt

# Select numeric columns
numeric_df = df[['Age', 'Avg_Daily_Screen_Time_hr', 'Educational_to_Recreational_Ratio']]

# Calculate correlation
corr_matrix = numeric_df.corr()

# Plot the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(
    data=corr_matrix,
    annot=True,                  # Show correlation numbers
    fmt=".2f",                   # Round numbers to 2 decimals
    cmap='coolwarm',             # Blue = negative, Red = positive
    linewidths=0.6,              # Lines between squares
    cbar_kws={"shrink": 0.8}    # Adjust color bar size
)
plt.title("Correlation Between Age, Screen Time & Educational/Rec Ratio", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Features", fontsize=12, fontweight='bold')
plt.ylabel("Features", fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()

# We Start The Week 4 – Advanced Visualizations

# Distribution plots with hue (screen time by gender)  its use ( True Values ) 
import seaborn as sns
import matplotlib.pyplot as plt

# Histogram for Screen Time
plt.figsize=(10,6)
sns.histplot(
    data=df,
    x='Avg_Daily_Screen_Time_hr',
    kde=True,
    bins=25,
    color='red',
    edgecolor='black'
)
plt.title('Distribution of Screen Time')
plt.xlabel('Screen Time (hours per day)')
plt.ylabel('Number of Students')
plt.show()


# Stacked barplots (device usage by location)

import pandas as pd
import matplotlib.pyplot as plt

# Create a cross-tab of Primary_Device by Location [ Urban or Rural]
device_location = pd.crosstab(df['Primary_Device'], df['Urban_or_Rural'])

# Plot stacked bar chart
device_location.plot(
    kind='bar',
    stacked=True,
    figsize=(8,6),
    color=['orange', 'Green'],
    edgecolor='black'
)
plt.title("Device Usage by Location", fontsize=14, fontweight='bold')
plt.xlabel("Device Type", fontsize=12)
plt.ylabel("Number of Students", fontsize=12)
plt.xticks(rotation=0)  # Keep X-axis labels horizontal
plt.legend(title="Location")

plt.tight_layout()
plt.show()


# Swarmplots / stripplots (screen time spread)

import seaborn as sns
import matplotlib.pyplot as plt

plt.figsize=(10,6)

# Create swarmplot to show representatio of screen time by gender
sns.swarmplot(
    data=df,
    x='Gender',
    y='Avg_Daily_Screen_Time_hr',
    palette='Set2',
    size=6
)
plt.title("Spread of Average Daily Screen Time by Gender", fontsize=14, fontweight='bold')
plt.xlabel("Gender", fontsize=12)
plt.ylabel("Avg Daily Screen Time (hours)", fontsize=12)

plt.tight_layout()
plt.show()

# Swarmplots / stripplots (screen time spread by device ) 

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,6))
sns.swarmplot(
    data=df,
    x='Primary_Device',
    y='Avg_Daily_Screen_Time_hr',
    hue='Gender',
    palette='Set2',
    alpha=0.8
)
plt.title("Swarmplot: Screen Time Spread by Device & Gender", fontsize=16)
plt.xlabel("Primary Device")
plt.ylabel("Average Daily Screen Time (hours)")
plt.xticks(rotation=45)
plt.legend(title="Gender", bbox_to_anchor=(1.05, 1))
plt.show()


# Combine multiple plots into subplot 

g = sns.FacetGrid
(df, col='Gender',
row='Primary_Device',
height=4, 
aspect=1.2
)
g.map(sns.histplot,
      'Avg_Daily_Screen_Time_hr',
      kde=True)
g.fig.suptitle('Distribution of Average Daily Screen Time by Primary Device and Gender',
               y=1.03
              )
g.set_axis_labels('Average Daily Screen Time (hours)', 'Frequency')

plt.tight_layout()

plt.show()



