import pandas as pd
cell = pd.read_csv("cellphones.csv")
population = pd.read_csv("population.csv")
cell_pop = cell.merge(population, how ="inner", on =["Country", "year"])
cell_pop.head()
geo = pd.read_csv("geo_country.csv")
geo.rename(columns={"country": "geo", "name": "Country"}, inplace = True)
geo.columns

