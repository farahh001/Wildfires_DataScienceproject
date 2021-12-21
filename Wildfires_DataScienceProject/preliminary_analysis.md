# California Fire Detection

### Group Members
- Farah Sultana
- Nishanth Prajith

### Repository Structure
- `data`
  - `California_Fire_Incidents.csv`: Raw data from the kaggle for all fires in california from 2013 - 2019
  - `California_Fire_Cleaned.csv`: Cleaned 'California_Fire_Cleaned.csv`
  - `weather_data.csv`: Raw data weather data from the World Weather Online API
  - `cleaned.csv` : Combined dataset for modeling
- `code`
  - `etl_california_fire.py`: Cleans `California_Fire_Incidents.csv`
  - `etl_weather.py`: Cleans `weather_data.csv`
  - `cleaning.py` : Combines the two datasets
  - `exploratory_data_analysis.ipynb`: Includes descriptive statistics and charts. 

### Exploratory Analysis
Before Diving into our Machine learning model we have tried to clean the dataset and get to know the selected features that are good enough to modeling.

#### 1. About the Dataset:
We are using the dataset on wildfires from kaggle `California_Fire_Incidents.csv` which is a huge datasets. For Simplicity we cleaned it and got it down to a form `California_Fire_Cleaned.csv` with which we can work with. In the whole process of the wildfire analysis, it is a great deal to know the accurate situation of the weather.For that we have used World Weather Online API. Our combined dataset named `cleaned.csv` has been cleaned further for our modeling purpose. With this dataset, we will find patterns in the time of year and county in california related to the number of wildfires. 

#### 2. Our Cleaning Process:
We performed the cleaning process on the raw datasets which we have divided into wildfire data named `etl_california_fire.py`, weather data named `etl_weather.py` and  merged dataset `cleaning.py`. In order to create a reliable dataset, we have identified unnecessary columns, dropped them  and remove missing and erroneous data. We believe that the  downsized dataset in the name of `cleaning.py` will help us  generate more accuate results while training  our machine learing model. 


#### 3. Data Visualization:
Apart from standard data science libraries there is a great selection of graphic libraries in which we used geospatial tools to visualize wildfires distribution which is the most exciting part of our analysis.
We have gathered valuable understanding and new insights through plotting.Many relations in our data are visualized using pandas and Folium which gave us  access to latitude and longitude and this way we put together a map. To get a sorted Order we used value_counts where  we get access to unique occurrences of columns “Counties” & “FIPS” and we framed it using the to_frame() function. We would analyze the wildfire by counties, for that matter we turned columns “Total_Fires” and “FIPS” into a list with the help of to_list.  “Total_Fires”  and the FIPS code which are assigned by county which will be analyzed  using choropleth().  From that we noticed that Riverside had the most wildfires  whereas Imperial County did not have any wildfires. You can find `exploratory_data_analysis.ipynb` in the code section of our repository.

### Challenges
One of the biggest challenges we faced so far was getting the weather information. Many weather API's did not have historical weather data information we were looking to use in our model. It was very difficult to find a reliable yet free API that will give us the information we required. But luckily World Weather Online API did manage to work out in the end. Another challenge we encountered was definitely with the jupyter notebook as we were trying to plot certain graphs on state maps which did not work out as planned, as google colab for some reason did detect the necessary libraries even though they were installed. But after some heavy debugging it did manage to work and resolve itself.

### Future Work
We are looking to explore more using the data and try differnt classification models to test which model is best. One of the things we will be looking to do is add data of time and places where there did not occur any fires so as to make the dataset more realistic. This should prevent the model from overfitting and help the model to be more accurate.

The Questions We’ll address to Predict and Analyze Wildfire Patterns

1. What role does environmental/geographical factors play? This will help us understand on which counties are more prone to destructive wildfires.
2. Which County had the most destructive wildfires?
3. How many acres per county are burnt by Wildfires?
4. Has the number of wildfires increased in counties over the year?

### Contributions
We both worked on the dataset cleaning and exploratory analysis. Nishanth mainly worked on data cleaning/fetching and Farah worked on some cleaing but mainly worked on the exploratory data analysis notebook.
