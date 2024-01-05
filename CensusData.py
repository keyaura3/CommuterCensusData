import requests
import csv
import pandas

r = requests.get("https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36")
r_text = r.text
r_json = r.json()

with open('commute_data.csv', mode = 'w', newline = '') as file:
  writer = csv.writer(file)
  writer.writerows(r.json())


commute_df = pandas.read_csv('commute_data.csv')
commute_df.columns = ['County, State', 'Total Commuters', 'Total', "90 min or more", ""]
print(commute_df.head())
