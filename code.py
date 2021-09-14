import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_excel('Car-Data.xlsx')
df.info()

df.describe()

df.corr()

sns.heatmap(df.corr())

df.head()

#Some of the column names in the file were written with a hyphen, I needed to change this. There were two ways to do it, one was to programatically read the column names and remove the hypens or go physically in the file and remove the hypens in the column names. I used the latter, since that is much more easier.

# check the total count of rows in the data frame
df.count()
df.info()

df.symboling.isnull().count()
df.make.isnull().count()
df.fueltype.isnull().count()
df.normalizedlosses.isnull().count()

#Lets look at the values of each of the columns and see if there are any null values of other junk characters and if there are any junk characters then lets replace it by 0 for all the numeric colomns

df.price.replace({"?":0},inplace=True)

#Let's convert some of the columns from string to float. Since the data type for price is defined as string and we need to convert to float

#df=df.astype('price':np.float).dtypes
#df=df.astype({'price':'int32'}).dtypes
df[["price"]]=df[["price"]].apply(pd.to_numeric)

#Lets build a distribution plot, which depicts the bar chart of which car in what price ranges are sold the most. If you see the chart below you see that most of the cars sold are in the price range from 5K to 25K

sns.distplot(df[['price']].apply(pd.to_numeric),kde=False,bins=20)

sns.distplot(df['highwaympg'],kde=False,bins=10)

#Now lets look at where the majority of the cars fall in segments such as the bore or stroke category. Before that we need to convert this string value column to numeric column and then there are certain values in this column which are ?, we need to replace all ? values with 0

df.head()

df.bore.replace({"?":0},inplace=True)
df.stroke.replace({"?":0},inplace=True)
#df[["bore"]]=df[["bore"]].apply(pd.to_numeric(downcast='float'))
df[["bore"]]=df[["bore"]].apply(pd.to_numeric)
df[["stroke"]]=df[["stroke"]].apply(pd.to_numeric)
#sns.distplot(df[['stroke']].apply(pd.to_numeric),kde=False,bins=20)
sns.distplot(df[['stroke']],kde=False,bins=20)

#Based on the above graph, we can see that most of the vehicles are in the 3 to 4 stroke category

sns.distplot(df[['bore']],kde=False,bins=20)

df.normalizedlosses.replace({"?":"?*"},inplace=True)
df.head()

sns.heatmap(df.isnull(),yticklabels=False)

# Now lets perform a box plot analysis on various numeric columns to understand what the outliers are. How should we manage those outliers?

# If we look at price then we notice that most of the price variants fall in between 8k to 28K range and few of the extreme outliers are above 40K in price.

# If we look at the wheel base we notice that majority of the case wheel base falls in between 95 and 113. The outlier here is with one falling in the 121 range.

df.boxplot('price')

# lets count various combination of columns to identify the preference for the number of doors for each make.

df.boxplot('wheelbase')

df.boxplot('curbweight')


# In the existing data lets look at some graph visualization of various categories such as engine location, number of cylinders the car has, drive wheel, bodystyle, number of doors etc. This is one aspect of data mining where one tries to understand the characteristics of the data in your data set.

# So if you see some basic mining excercises, most of the cars that are sold are with front engines. There is a significant amount of cars that are sold which are two door, which almost constitue around 80%+ of the total sales compared to four door sedans. The most popular body style cars are sedan and hatchback.

df['enginelocation'].value_counts().plot(kind='barh')

df['numofdoors'].value_counts().plot(kind='barh')

df['bodystyle'].value_counts().plot(kind='barh')

df['drivewheels'].value_counts().plot(kind='barh')

df['numofcylinders'].value_counts().plot(kind='barh')

sns.countplot(x='make',hue='numofdoors',data=df)


# Below is a sample of a simple data mining technique to understand which bodystyle cars with which fueltype are sold the most. Another sample of data mining is to understand which bodystyle cars with which engine location are sold the most.

sns.catplot(x="bodystyle", hue="make", col="fueltype",
                data=df, kind="count",
                height=4, aspect=1.3);

sns.catplot(x="bodystyle", hue="make", col="enginelocation",
                data=df, kind="count",
                height=4, aspect=1.3);

sns.catplot(x="bodystyle", hue="make", col="drivewheels",
                data=df, kind="count",
                height=4, aspect=1.4);

sns.catplot(x="bodystyle", hue="make", col="numofdoors",
                data=df, kind="count",
                height=4, aspect=1.3);
