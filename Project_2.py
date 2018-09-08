import warnings
from pylab import *
warnings.simplefilter('ignore', FutureWarning)

from pandas import *
import matplotlib.pyplot as plt, mpld3

# matplotlib.use('Qt4Agg')   # generate Qt4Agg by default

# Get the CSV file for Delhi_DEL_2014
delhi = read_csv('Delhi_DEL_2014.csv', skipinitialspace=True) # read and skip initial heading spaces

# NB the dataframe delhi now contains the following columns
#Index(['Date', 'Max TemperatureC', 'Mean TemperatureC', 'Min TemperatureC',
#       'Dew PointC', 'MeanDew PointC', 'Min DewpointC', 'Max Humidity',
#       'Mean Humidity', 'Min Humidity', 'Max Sea Level PressurehPa',
#       'Mean Sea Level PressurehPa', 'Min Sea Level PressurehPa',
#       'Max VisibilityKm', 'Mean VisibilityKm', 'Min VisibilitykM',
#       'Max Wind SpeedKm/h', 'Mean Wind SpeedKm/h', 'Max Gust SpeedKm/h',
#       'Precipitationmm', 'CloudCover', 'Events', 'WindDirDegrees'],
#      dtype='object')

# first view of the file
print("")
print('First view of the delhi file , first 5 records')
print("")
print(delhi.head())
print("")

# remove and HTML code from headings and data values
delhi = delhi.rename(columns={'WindDirDegrees<br />' : 'WindDirDegrees'}) # correct column lable text
delhi['WindDirDegrees'] = delhi['WindDirDegrees'].str.rstrip('<br />') # remove Trainling HTML code column data cell

# output so fare
print ("The table for Delhi 2014 , after HTML code has been removed!")
print(delhi.head())
print("")

# change datatype for WindDirDegrees to float64

# first displat the current columns and data type
print("The columns in the delhi file")
print (delhi.columns)
print("")
print("The data types of WindDirDegrees column, will be converted to float64, currently is - ")
print ("WindDirDegrees :",delhi['WindDirDegrees'].dtypes)
print("")

# convert the WindDirDegrees column data type to float64
delhi['WindDirDegrees'] = delhi['WindDirDegrees'].astype('float64')   # convert column WindDirDegrees to a 64bit real

# Output file as is
print("")
print("The data types of these WindDirDegrees columns after type conversion ")
print ("WindDirDegrees :",delhi['WindDirDegrees'].dtypes)
print("")

# convert the Date column data type to datetime64
print("Convert Date to datetime")
print("")
print ("Current data type for Date: ",delhi['Date'].dtypes)
print("")

delhi['Date'] = to_datetime(delhi['Date']) # convert column WindDirDegrees to a 64bit real

# Output file as is
print("")
print("The data types of these Datecolumns after type conversion ")
print ("Date : ",delhi['Date'].dtypes)
print("")

# now change the index , by Date
delhi.index = delhi['Date'] # Index table on Sample 'Date' field.

print("Show that the Index is now by date")
print(delhi.head())
print("")


# Finding a summer break


#According to the website http://www.delhitourism.gov.in/delhitourism/aboutus/seasons_of_delhi.jspmeteorologists,
# the summer season in India extends for
#the whole months of April to June. The Monsoon period is from July to Mid-September.
#I do not want to go to India during the Monsoon season. Therefore, I'm going to create a dataframe that holds just the
#  summer months using the datetime index, like this:

summer = delhi.loc[datetime(2014,4,1) : datetime(2014,6,30)] # select a new dataframe for the dates of the Indian summer
print("")
print("Data frame summer , dates from start of April to June 2014")
print("")
print("File header")
print("")
print(summer['Date'].head())
print("File tail")
print(summer['Date'].tail())
print("")

# I want to look for the days with warm temperatures ideally warmer than 22 Celsius and cooler than 28 Celsius.

# A select a new dataframe for the dates of the Indian summer
indianSummer = delhi.loc[datetime(2014,4,1) : datetime(2014,6,30)]

# B select only dates that have a Mean temp within my chosen range
summer = indianSummer[(indianSummer['Mean TemperatureC'] >= 22) & (summer['Mean TemperatureC'] <= 28)]

print("")
print("Show rows for dates of the Indian summer and Temps between (22 and 28 deg C")
print(summer[['Date','Mean TemperatureC']])
print("")

# ploting a graph outside of jupyter notes book for the selected dates and mean temperatures

fig, ax = plt.subplots()

ax.grid(linestyle='solid') # backgroup grid
ax.set_title("Delphi 2014 Mean Temperature Oc chart", size=10) # graph title
ax.set_ylabel('Mean Temperatures Oc(Red)',size=5) # left vertical title
ax.set_xlabel('Days for temps between 22 and 28 Deg C',size=5) # bottom horizontal title
ax.xaxis.set_tick_params(labelsize=5)
ax.yaxis.set_tick_params(labelsize=5)

print('See your web browser for a graphical output, press ctlr-c to continue this program')


plt.plot(summer['Mean TemperatureC'], 'ks-', mec='W', mew=1, ms=4, color='red')
#mpld3.display()
mpld3.show()


# ploting a graph outside of jupyter notes book for the selected dates and mean temperatures and Precipitationmm

fig, ax = plt.subplots()

ax.grid(linestyle='solid') # backgroup grid
ax.set_title("Delphi 2014 Mean Temperature Oc  and rain fall chart", size=10) # graph title
ax.set_ylabel('Mean Temperatures Oc(Red), Rain fall mm (Blue)',size=5) # left vertical title
ax.set_xlabel('Days for temps between 22 and 28 Deg C',size=5) # bottom horizontal title
ax.xaxis.set_tick_params(labelsize=5)
ax.yaxis.set_tick_params(labelsize=5)

print('See your web browser for a graphical output, press ctlr-c to continue this program')


plt.plot(summer['Mean TemperatureC'], 'ks-', mec='W', mew=1, ms=4, color='red')
plt.plot(summer['Precipitationmm'], 'ks-', mec='W', mew=1, ms=4, color='blue')
#mpld3.display()
mpld3.show()

#Although the rainfall in months 4 and 5 is acceptable, the combined results
#(rainfall and temp) rule out the months of April and May to travel because temperature is below optimum.

#The month of June shows optimum conditions. The first two weeks of June falls within an acceptable range,
# with just a couple of peaks showing some rain. The second two weeks of June have higher temperatures and
# I feel that I prefer the lower temperatures within the range specified. Therefore
# I have concentrated on the first two weeks of June.


# A select a new dataframe for the dates of the Indian summer
indianSummerJune = delhi.loc[datetime(2014,6,1) : datetime(2014,6,16)]

# B select only dates that have a Mean temp within my chosen range
summer = indianSummerJune[(indianSummer['Mean TemperatureC'] >= 22) & (summer['Mean TemperatureC'] <= 28)]

# ploting a final graph outside of jupyter notes book for the selected dates and mean temperatures and Precipitationmm

fig, ax = plt.subplots()

ax.grid(linestyle='solid') # backgroup grid
ax.set_title("Delphi 2014 Mean Temperature Oc and Rain fall chart", size=10) # graph title
ax.set_ylabel('Mean Temperatures Oc(Red), Rain Fall mm (Blue)',size=5) # left vertical title
ax.set_xlabel('Days for temps between 22 and 28 Deg C',size=5) # bottom horizontal title
ax.xaxis.set_tick_params(labelsize=5)
ax.yaxis.set_tick_params(labelsize=5)

print('See your web browser for a graphical output, press ctlr-c to continue this program')


plt.plot(summer['Mean TemperatureC'], 'ks-', mec='W', mew=1, ms=4, color='red')
plt.plot(summer['Precipitationmm'], 'ks-', mec='W', mew=1, ms=4, color='blue')
#mpld3.display()
mpld3.show()