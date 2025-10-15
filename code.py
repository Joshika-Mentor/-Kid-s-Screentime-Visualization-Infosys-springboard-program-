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



# --- Distribution of Screen Time by Device and Gender
# --- FACETGRID CREATION ---
sns.set_theme(style="whitegrid")
# Initialize the FacetGrid
g = sns.FacetGrid(
    df,
    col='Primary_Device',  # Separate plots into columns based on device
    hue='Gender',          # Separate lines/colors within each plot based on gender
    col_wrap=2,            # Display 2 columns per row
    height=4,
    aspect=1.2,
    sharey=False           # Allow density (Y-axis) scale to vary per plot
)
# Map the KDE (Kernel Density Estimate) plot onto the grid
g.map(
    sns.kdeplot,
    'Avg_Daily_Screen_Time_hr',
    fill=True,             # Fill the area under the curve
    alpha=0.6,
    linewidth=1.5
)
# Map a vertical line to show the overall mean screen time
g.map(
    plt.axvline,
    x=overall_mean,
    ls='--',
    color='gray',
    label='Overall Mean'
)
# --- 3. STYLING AND DISPLAY ---
g.add_legend(title='Gender')
g.set_axis_labels("Avg. Screen Time (hr)", "Density")
g.set_titles(col_template="{col_name} Users")
g.figure.suptitle('Distribution of Screen Time by Device and Gender', y=1.02, fontsize=16)
plt.show() # Display the plot



# --- PAIRPLOT CREATION ---
sns.set_theme(style="ticks")
# Create the pairplot
g = sns.pairplot(
    df,
    vars=numerical_cols,
    hue='Gender',           # Color the points based on Gender
    height=3,
    palette='deep',
    diag_kind='kde'         # Use KDE (density plots) on the diagonal
)
g.fig.suptitle('Pairwise Relationships of Numerical Variables, Colored by Gender', y=1.02)
plt.show()



# --- HEATMAP CREATION ---
plt.figure(figsize=(8, 6))
sns.heatmap(
    corr_matrix,
    annot=True,              # Show the correlation values
    cmap='coolwarm',         # Divergent color map (blue for negative, red for positive)
    fmt=".2f",               # Format values to 2 decimal places
    linewidths=.5,           # Add lines between cells
    cbar_kws={'label': 'Correlation Coefficient'}
)
plt.title('Correlation Heatmap of Key Numerical Variables', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()



#Distribution plots with hue (screen time by gender)
plt.figure(figsize=(10, 6))
sns.histplot(
    df,
    x='Avg_Daily_Screen_Time_hr',
    # Use 'hue' to segment the distribution by the 'gender' column
    hue='Gender',
    # Add a Kernel Density Estimate line for a smoother visualization
    kde=True,
    palette={'Male': 'skyblue', 'Female': 'salmon'},
    # 'stat="density"' normalizes the heights so the total area of the histogram equals 1
    stat='density',
    # 'common_norm=False' ensures each gender's distribution is normalized independently
    common_norm=False
)
plt.title('Distribution of Average Daily Screen Time by Gender')
plt.xlabel('Average Daily Screen Time (hours)')
plt.ylabel('Density')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# ---  Stacked barplots (device usage by location) ---
plt.figure(figsize=(8, 5))
# Use the pandas plot method with the stacked=True argument
device_location_proportions.plot(
    kind='bar', 
    stacked=True, 
    cmap='viridis',
    ax=plt.gca() # Plot onto the figure we just created
)
# --- STYLING ---
plt.title('Proportional Device Usage by Location Type')
plt.xlabel('Location Type')
plt.ylabel('Proportion of Devices (%)')
plt.xticks(rotation=0) # Keep 'Urban' and 'Rural' labels horizontal
plt.legend(title='Primary Device')
plt.tight_layout()
plt.show()


# --- Swarmpplots (device usage by location)
sns.swarmplot(
    data=df,
    x='Primary_Device',
    y='Avg_Daily_Screen_Time_hr',
    hue='Gender'
)
plt.show()



# --- Stripplots (device usage by location)
plt.figure(figsize=(8, 5))
sns.stripplot(
    data=df,
    x='Gender',
    y='Avg_Daily_Screen_Time_hr',
    jitter=0.2,
    size=8,
    linewidth=1
)
plt.title('Screen Time Spread by Gender (Stripplot)')
plt.xlabel('Gender')
plt.ylabel('Avg. Daily Screen Time (Hours)')
plt.show()



# 1. Create a Figure and a 1x2 Grid of Axes
# fig: the overall container
# axes: an array containing the two subplot areas (ax1 and ax2)
fig, axes = plt.subplots(
    nrows=1, 
    ncols=2, 
    figsize=(14, 6) # Overall figure size
)
# --- Subplot 1: Histogram/KDE (placed on axes[0]) ---
sns.histplot(
    data=df, 
    x='Avg_Daily_Screen_Time_hr', 
    kde=True, 
    hue='Gender',
    ax=axes[0] # << KEY: Specify the target axis
)
axes[0].set_title('Screen Time Distribution')
# --- Subplot 2: Swarmplot (placed on axes[1]) ---
sns.swarmplot(
    data=df, 
    x='Primary_Device', 
    y='Avg_Daily_Screen_Time_hr', 
    hue='Gender',
    ax=axes[1], # << KEY: Specify the target axis
    dodge=True
)
axes[1].set_title('Screen Time Spread by Device')
axes[1].legend().remove() # Remove redundant legend from the second plot
# 2. Add an overall title and adjust spacing
fig.suptitle('Comparative Analysis of Screen Time', fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.96]) # Adjust spacing for suptitle
plt.show()
