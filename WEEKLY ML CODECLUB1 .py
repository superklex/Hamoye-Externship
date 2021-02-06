import pandas as pd
import numpy as np

#loading the cellphones dataset
cell = pd.read_csv("cellphones.csv")

#loading the population dataset
population = pd.read_csv("population.csv")

#new dataframe from the merging cellphone and population dataframe
cell_pop = cell.merge(population, how ="inner", on =["Country", "year"])

#verifying the shape of the merged datataframe
cell_pop.shape

#loadingg the geo_country dataset
geo_country = pd.read_csv("geo_country.csv")

#renaming columns and verifying
geo_country.rename(columns={"country": "geo", "name": "Country"}, inplace = True)
geo_country.columns

#adding columns to the "new" dataframe
new = pd.merge(cell_pop, geo_country[["geo", "Country"]], how="left")
new.head

#adding a new column that shows the average cellphone per person
new["cell_phone_per-person"] = new["cell_phones_total"]/new["population"]
new.head

#verifying the number of cellphone per person in United States for 2017
new.loc[(new['Country'] == "United States") & (new["year"] == 2017 )]

#making the geocodes uppercase
new["geo"].str.upper()

#describing the dataframe
new.describe()

#check for unique countries
new["Country"].nunique()