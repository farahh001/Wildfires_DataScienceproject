
import pandas as pd # need to have pandas installed
import addfips # AddFIPS is a tool for adding state or county FIPS codes to files that contain just the names of those geographies.

# Cleaning California_Fire_Incidents.csv

# Read the kaggle dataset we downloaded
dataset = pd.read_csv('../data/California_Fire_Incidents.csv')
print(dataset.columns)

remove_column_names = ['SearchDescription', 'SearchKeywords', 'StructuresDamaged', 'StructuresDestroyed',
       'StructuresEvacuated', 'StructuresThreatened', 'UniqueId', 'Updated',
       'WaterTenders', 'AirTankers', 'CanonicalUrl', 'ConditionStatement', 'ControlStatement',  'CrewsInvolved', 'Dozers',
       'Engines', 'FuelType', 'Helicopters', 'PersonnelInvolved', 'Active', 'Public']   # remove columns we do not need

dataset = dataset.drop(columns = remove_column_names)

format_String = "%Y-%m-%dT%H:%M:%SZ" # Format style for the date and time columns
dataset['Extinguished'] = pd.to_datetime(dataset['Extinguished'], format = format_String) # Format time

# Remove microseconds from data and convert to datetime format above
for i in dataset.index:
  if (len(dataset['Started'][i]) > 20):
    dataset['Started'][i] = dataset['Started'][i][:19] + "Z"

dataset['Started'] = pd.to_datetime(dataset['Started'], format = format_String)

print(dataset.dtypes)

dataset['Active Time'] = dataset['Extinguished'] - dataset['Started'] # Calculate the active time of the fire aka the total time the fire was active before it was extinguished

dataset['FIPS'] = int(0) # create a new column for the FIPS code which is initially set to 0

af = addfips.AddFIPS()

for i in dataset.index:
  a = af.get_county_fips(dataset['Counties'][i], state='California') # get the FIPS code for the county
  if a != None:
    dataset['FIPS'][i] = int(af.get_county_fips(dataset['Counties'][i], state='California')) # Convert the FIPS code to an integer
  else :
    dataset['FIPS'][i] = None

dataset.to_csv('../data/California_Fire_Cleaned.csv')