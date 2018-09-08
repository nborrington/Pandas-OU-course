import warnings
from pylab import *
warnings.simplefilter('ignore', FutureWarning)

from pandas import *
import matplotlib.pyplot as plt, mpld3

matplotlib.use('Qt4Agg')   # generate Qt4Agg by default


# Exercise 1: Dataframes and CSV files

# To read a CSV file into a dataframe you need to call the pandas function called read_csv().
# The simplest usage of this function is with a single argument, a string that holds the name of the CSV file,
# for example.


# Read in the Who popluation to TB deaths statistics file with headings : (Country,Population (1000s),TB deaths)
df = read_csv('WHO POP TB all.csv') # load csv file into df dataframe

# Dataframes have attributes as follows (https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html)
# they are :
# (T 	Transpose index and columns.
#at 	Access a single value for a row/column label pair.
#axes 	Return a list representing the axes of the DataFrame.
#blocks 	(DEPRECATED) Internal property, property synonym for as_blocks()
#columns 	The column labels of the DataFrame.
#dtypes 	Return the dtypes in the DataFrame.
#empty 	Indicator whether DataFrame is empty.
#ftypes 	Return the ftypes (indication of sparse/dense and dtype) in DataFrame.
#iat 	Access a single value for a row/column pair by integer position.
#iloc 	Purely integer-location based indexing for selection by position.
#index 	The index (row labels) of the DataFrame.
#ix 	A primarily label-location based indexer, with integer position fallback.
#loc 	Access a group of rows and columns by label(s) or a boolean array.
#ndim 	Return an int representing the number of axes / array dimensions.
#shape 	Return a tuple representing the dimensionality of the DataFrame.
#size 	Return an int representing the number of elements in this object.
#style 	Property returning a Styler object containing methods for building a styled HTML representation fo the DataFrame.
#values)

# to display them following
print('----------------------------------------------------------------------------------')
print('The dataframe for the WHO population to TB deaths , contains the following columns',df.columns)
print('')

# Selecting datafram rows using an index number
#
# A dataframe has a default integer index for its rows, which starts at zero 0. The iloc attribute can be used to
# obtain the row at the given index.

print(df.iloc[0]) # first row, index 0
print('')
print(df.iloc[2]) # third row, index 2
print('')

# The .head() method
import matplotlib.pyplot as plt, mpld3

matplotlib.use('Qt4Agg')   # generate Qt4Agg by default
# The .head() method returns a dataframe with the first rows,
# as many as given in the argument. By default, if the argument is missing, it returns the first five rows.

print('the df.head() method used to print the first 5 or a given value of rows', df.head()) # first five rows
print('')

# The .tail() method

# The .tail() method returns a dataframe with the last rows,
# as many as given in the argument. By default, if the argument is missing, it returns the last five rows.

print('the df.tail() method used to print the first 5 or a given value of rows', df.tail()) # last five rows
print('')

# Selecting multi dataframe columns for .head() or .tail(), using a list

df_head = df[['Country', 'Population (1000s)']].head(10)
print("using , df_head = df[['Country', 'Population (1000s)']].head(10) to print head of a multi column selection")
print(df_head)
print('')

# Selecting multi dataframe columns for .head() or .tail(), using a list

df_tail = df[['Country', 'Population (1000s)']].tail(10)
print("using , df_tail = df[['Country', 'Population (1000s)']].tail(10) to print tail of a multi column selection")
print(df_tail)
print('')

# Applying attributes and methods to a single datafram column

# The iloc() attribute and the head() and tail() methods discussed above can be used with single columns.

print('')
print('TB deaths from df.iloc[2] column = ',df['TB deaths'].iloc[2]) # print the third value of deaths column
print('')
# Print the last five values of population column
print('The last five rows of the Population column in dataframe df = ',df['Population (1000s)'].tail())
print('')

# get and display the 55th row in the dataframe df

print('The dataframe df at location iloc(55) contains the :')
print(df.iloc[55])
print('')

# first 10 rows of the dataframe df

print('first 10 rows of the dataframe df')
print(df.head(10))
print('')

#  select and display the first eight rows from the 'Country' and 'TB deaths' columns.

County_deaths_first_10 = df[['Country','TB deaths']]
print("The first eight rows of the 'Country' and 'TB deaths' columns are :")
print(County_deaths_first_10.head(8))
print('')

# Albania's Population and TB deasths using .iloc[x]

print ('Albania (row 2) has a population of : ',df['Population (1000s)'].iloc[1],'With ',df['TB deaths'].iloc[1],'deaths from TB')
print('')

# Exercise 2: Comparison operators

#Python has the following comparison operators:

# == (equals)
# != (not equal)
# < (less than)
# > (greater than)
# <= (less than or equal to)
# >= (greater than or equal to)

# The following code will get and display all the rows in df where it is True that the value in the
# 'Population (1000s)' column is greater than 80000.

rows_With_pop_over_80000 = df[df['Population (1000s)'] > 80000]
print('The following countries have a population over 80000')
print(rows_With_pop_over_80000)
print('')

# df where TB deaths exceed 10000

rows_With_TBdeaths_over_10000 = df[df['TB deaths']> 10000]
print('The following countries have a death rate of over 10,000 from TB')
print(rows_With_TBdeaths_over_10000)
print('')


# Exercise 3: Bitwise operators

# Pandas has two operators to make more complicated queries. Use the operator & (means 'and') to select rows where two
# conditions are both true. Use the operator | (means 'or') to select rows where at least one condition is true.
# Don't forget to put parentheses around each comparison. For example, the following expression selects only countries
#  with a population over 80 million inhabitants and with more that 10 thousand deaths.

# & (means 'and')
# | (means 'or')

rows_With_Pop_And_TBdeaths_Over_80000_And_10000_respectfully \
    = df[(df['Population (1000s)'] > 80000) & (df['TB deaths'] > 10000)]
print('The following countries have a Population over 80,0000 death rate of over 10,000 from TB')
print(rows_With_Pop_And_TBdeaths_Over_80000_And_10000_respectfully)
print('')

# If the same columns will be used repeatedly in the program, the code becomes more readable if written as follows:
# population = df['Population (1000s)']
# deaths = df['TB deaths']
# df[(population > 80000) & (deaths > 10000)]

# countries where the Population (1000s) is less than or equal to 50000 or TB deaths are greater than or equal to 20000.

population = df['Population (1000s)']
deaths = df['TB deaths']
rows_With_Pop_And_TBdeaths_LessthanEqualto_80000_Or_GreaterThanEqualto_20000_respectfully = df[(population <= 50000) | (deaths >= 20000)]
print('Countries where the Population (1000s) is less than or equal to 50000 or TB deaths are greater than or equal to 20000.')
print(rows_With_Pop_And_TBdeaths_Over_80000_And_10000_respectfully)
print('')

# Exercise 4: Display rows from dataframe

# You have downloaded the file London_2014.csv from our website, it can now be read into a dataframe.

london = read_csv('London_2014.csv')
print('The london weather underground dataframe has the following columns')
print(london.columns)
print('')
print('It contains the following data')
print('')
print(london.head())
print('')

# Removing initial spaces from column headings

london = read_csv('London_2014.csv', skipinitialspace=True)

# now show the new column headings
print('We have removed any leading spaces from the colnum names as follows :')
print(london.columns)

# Removing extra characters

# Another problem shown above is that the final column is called 'WindDirDegrees< br />'.

# When the dataset was exported from the Weather Underground web site html line breaks were automatically added
# to each line in the file which read_csv() has interpreted as part of the column name and its values.
# This can be seen more clearly by looking at more values in the final column:

print('As you can see the Wind Degrees column has unwanted characters <br />')
print(london['WindDirDegrees<br />'].head())
print('')

 # 'WindDirDegrees< br />' can be changed to 'WindDirDegrees' with the rename() method as follows:

london = london.rename(columns={'WindDirDegrees<br />' : 'WindDirDegrees'})
print(" Remove the unwanted HTML code ")
print('See code line 201')
print(london.columns)
print('')

# To remove the '< br />' html line breaks from the values in the 'WindDirDegrees'
# column you need to use the string method rstrip() which is used to remove characters
# from the end or 'rear' of a string:

print('Method .rstrip is used to remove the unwated characters from the WinDirDegrees column data ')
london['WindDirDegrees'] = london['WindDirDegrees'].str.rstrip('<br />')
print (london['WindDirDegrees'].head())
print('')

# Missing values

# Missing (also called null or not available) values are marked as NaN (not a number) in dataframes.

print('The column Events has some missing values as follows:')
print(london['Events'].tail())

# The isnull() method returns True for each row in a column that has a null value. The method can be used to select
# and display those rows. Scroll the table below to the right to check that the events column is only
# showing missing values.

print('The method .isnull() can be used to show these rows , the NaN rows')
london_Nan_Event_Rows = london[london['Events'].isnull()]
print(london_Nan_Event_Rows['Events'])
print('')

# One way to deal with missing values is to replace them by some value. The column method fillna()
# fills all not available value cells with the value given as argument.
# In the example below, each missing event is replaced by the empty string.
london_Nan_Event_Rows_fillna = london
london_Nan_Event_Rows_fillna['Events']=london_Nan_Event_Rows_fillna['Events'].fillna('')
# london_Nan_Event_Rows_fillna = london_Nan_Event_Rows_fillna[london_Nan_Event_Rows_fillna['Events'].isnull()]
print('New dataframe with NaN data rows removed, as you can see below :')
print('Check code line 243 to 248')
print(london_Nan_Event_Rows_fillna[london_Nan_Event_Rows_fillna['Events'].isnull()])
print('')

#The empty dataframe (no rows) confirms there are no more missing event values.

#Another way to deal with missing values is to ignore rows with them. The dropna() dataframe method returns a new
# dataframe where all rows with at least one non-available value have been removed.

london_NaN_Dropped = london.dropna()
print('London weather data with NAN data droped')
print(london_NaN_Dropped)
print('')
print('Note the following is the last row with its index number for london , with NaN rows')
print(london.tail(1))
print('')

# Changing the value type of a column

# The type of every column in a dataframe can be determined by looking at the dataframe's dtypes attribute, like this:

# Output the data types of all columns

print('The data types of the Columns in the london weather dataframe is as follows')
print(london.dtypes)
print('')

# The type of all the values in a column can be changed using the astype() method. The following code will change
# the values in the 'WindDirDegrees' column from strings (object) to integers (int64).

london['WindDirDegrees'] = london['WindDirDegrees'].astype('int64')

print('Changed column WindDirDegrees from type Object to  int64')
print(london['WindDirDegrees'].dtypes)
print('')

# The function to_datetime() is needed to change the values in the 'GMT'
# column from strings (object) to dates (datetime64):

london['GMT'] = to_datetime(london['GMT'])
print('The data type for the GMT column has been change from object to :',london['GMT'].dtypes)
print('')

print('The data types of the Columns in the london weather dataframe is now as follows')
print(london.dtypes)
print('')

# Values of type datetime64 can be created using the datetime() function where the first integer argument is the year,
# the second the month and the third the day. The code below will get and display the row in the
# dataframe whose 'GMT' value is 4th June 2014.

print('Selecting weather data for date 2014 - 6 - 4')
print(london[london['GMT'] == datetime(2014, 6, 4)])
print('')

# Queries such as 'Return all the rows where the date is between 8 December and 12 December' can be made:

dates = london['GMT']
start = datetime(2014, 12, 8)
end = datetime(2014, 12, 12)

print('Return all the rows where the date is between 8 December and 12 December')
print(london[(dates >= start) & (dates <= end)])
print('')

# Now that the wind direction is given by a number, write code to select all days that had a northerly wind. Hint:
# select the rows where the direction is greater than or equal to 350 or smaller than or equal to 10, as the compass
# rose shows.

print('in London a select all days that had a northerly wind >= 350 or <= 10')
# Select all rows where the wind direction was north
LondonWindDirectionNorth = london[(london['WindDirDegrees'] >= 350) | (london['WindDirDegrees'] <= 10)]
# Output all rows in the london data with a wind direction of north sorted by WindDirDegrees
print(LondonWindDirectionNorth.sort_values('WindDirDegrees'))
print('')

# In the code cell below, write code to get and display all the rows in the
# dataframe that are beween 1 April 2014 and 11 April 2014.

dates = london['GMT'] # select the GMT dates column
startDate = datetime(2014, 4, 1) # assign a starting date for the below search
endDate = datetime(2014,4,11) # assign a ending date for the below search
# select the row in the date range (startDate : endDate)
LondonDateRangeSelection = london[(dates >= startDate) & (dates <= endDate)]
# Output datarange sorted by date
print('Select the row in the date range (2014,4,1 : 2014,4,11)')
print(LondonDateRangeSelection.sort_values('GMT'))
print('')

# In the cell below, write two lines of code to display the first five rows that have a missing value in the
# 'Max Gust SpeedKm/h' column. Hint: first select the missing value rows and store them in a new dataframe,
# then display the first five rows of the new dataframe.

print('first five rows with missing value in Max Gust SpeedKm/h column.')
print(london[london['Max Gust SpeedKm/h'].isnull()].head(5))
print('')

# Exercise 5: Every picture tells a story

# NB needs the following two lines

# import matplotlib.pyplot as plt, mpld3

# matplotlib.use('Qt4Agg')   # generate Qt4Agg by default

# ploting a graph outside of jupyter notes book

fig, ax = plt.subplots()

ax.grid(linestyle='solid') # backgroup grid
ax.set_title("London 2014 (Wind speed Km/h, Rain fall mm and Temperature Oc) chart", size=10) # graph title
ax.set_ylabel('Wind speed Kmh(red), Rain mm(blue), Temp Oc(Orange)',size=5) # left vertical title
ax.set_xlabel('Days of the year',size=5) # bottom horizontal title

# The following line of code tells python to plot a  graph that is created using mpld3.
# plot Max Windspeed Km/h



# plot 'Max Wind SpeedKm/h','Mean Wind SpeedKm/h'

print('See your web browser for a graphical output, press ctlr-c to continue this program')

plt.plot(london['Max Wind SpeedKm/h'], 'ks-', mec='W', mew=1, ms=4, color='red')
plt.plot(london['Precipitationmm'], 'ks-', mec='W', mew=1, ms=4, color='blue')
plt.plot(london['Max TemperatureC'], 'ks-', mec='W', mew=1, ms=4, color='orange')
#mpld3.display()
mpld3.show()


fig, ax = plt.subplots()

ax.grid(linestyle='solid') # backgroup grid
ax.set_title("London 2014 (Mean Humidity chart) chart", size=10) # graph title
ax.set_ylabel('Mean Humidity (Orange)',size=5) # left vertical title
ax.set_xlabel('Days of the year',size=5) # bottom horizontal title
ax.xaxis.set_tick_params(labelsize=5)
ax.yaxis.set_tick_params(labelsize=5)

# plot mean humidity during spring (March, April and May)

londonSpringTime = london

londonSpringTime.index = london['GMT'] # change the index

londonSpringTime = london.loc[datetime(2014, 3, 1) : datetime(2014, 5, 31)] # select springtime dates

print(londonSpringTime.head)
plt.plot(londonSpringTime['Mean Humidity'], 'ks-', mec='W', mew=1, ms=4, color='orange')
#mpld3.display()
mpld3.show()

print('Finished')