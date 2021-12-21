# -*- coding: utf-8 -*-
"""etl_weather.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1imbBfUVSxx3kvYwEORyZR5_I-HfQRXmh
"""

import pandas as pd
import requests
import datetime

dataset = pd.read_csv("../data/California_Fire_Cleaned.csv") # Read the wildfire cleaned data

len(dataset['Counties'])

new = dataset[['FIPS', 'Latitude', 'Longitude', 'Counties', 'Started']] # Create a new dataframe with the filters columns from the wilfire dataset

# Create new columns for the data intialize all of them to zero. We will populate these columns with data later
new[['Temp Day One', 'Temp Day Two', 'Temp Day Three', 'Temp Day Four', 'Temp Day Five']] = 0.0

new[['MaxTemp Day One', 'MaxTemp Day Two','MaxTemp Day Three','MaxTemp Day Four', 'MaxTemp Day Five']] = 0.0

new[['MinTemp Day One','MinTemp Day Two','MinTemp Day Three','MinTemp Day Four','MinTemp Day Five']] = 0.0

new[['Humidity Day One','Humidity Day Two','Humidity Day Three','Humidity Day Four','Humidity Day Five']] = 0.0

new.head(3)

new.dtypes

new = new.loc[new['Latitude'] != 0] # Drop latitude and longitude with 0 since california does 
new = new.loc[new['Longitude'] != 0] # not have any counties with latitude or longitude equal to 0
new = new.loc[new['Longitude'].notnull()] # remove null values
new = new.loc[new['Latitude'].notnull()] # remove null values
new = new.reset_index(drop=True) # reset the index

len(new)

def storeData(a, j):
  columnName_one = ['Temp Day', 'MaxTemp Day', 'MinTemp Day', "Humidity Day"] # Create a list of column names
  columnName_two = ["One", "Two", "Three", "Four", "Five"] # List of the day counts
  # The above is done like this to make it easier

  dataName = ["avgtempF", "maxtempF", "mintempF"] # JSON data name

  for i in range(0, 5):
    for k in range(0, 3):
      v = columnName_one[k] + " " + columnName_two[i]
      k = dataName[k]
      new[v][j] = a[i][k]
    
    avg = 0.0
    b = a[i]['hourly']
    
    # loop that calculates the average humidity for each day
    for g in range(0, 8):
      avg += float(b[g]['humidity'])
    avg = float(avg / 8)
    v = "Humidity Day " + columnName_two[i]
    new[v][j] = avg

days = datetime.timedelta(5) # 5 days
day = datetime.timedelta(1)  # 1 day
apiKEY = "" # Add API key here
a = {}
c = {}
l = len(new)
for j in range(l):
  lat = new['Latitude'][j]
  longi = new['Longitude'][j]
  endDate = str(pd.to_datetime(new['Started'][j]) - day)[0:10] # date the day before the fire started
  startDate = str(pd.to_datetime(new['Started'][j]) - days)[0:10] # 5 days before the fire started

  requestLink = "http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key={key}&q={lat},{longi}&format=json&date={start}&enddate={end}".format(key = apiKEY, start = startDate, end = endDate, lat = lat, longi = longi)

  data = requests.get(requestLink)

  c = data
  try :
    a = data.json()['data']['weather'] # Get the API json weather data
    storeData(a, j) # run the function to filter and store the data (a is the json data and j is the index of the current row in the dataframe)
  except Exception as e:
    print(e)



new = new.loc[new['Temp Day One'] != 0.0] # Drop the rows with 0 temperature values
new = new.reset_index(drop=True) # reset the index

new.to_csv("../data/weather_data.csv") # Store the dataframe in a csv file