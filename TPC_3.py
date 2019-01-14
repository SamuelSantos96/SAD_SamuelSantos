from sklearn import datasets
import pandas as pd
import numpy as np

# Import data to variable
data = datasets.california_housing.fetch_california_housing() 

dados = np.column_stack((data.data,data.target))

newfeature = data.feature_names + ["Valor"] 

# Data Frame
df = pd.DataFrame(dados, columns = newfeature)
df.head()

agregar = df.groupby("MedInc").agg(["max"])  
agregar

# Sampling
print("-----------------SAMPLING----------------\n", np.random.random_sample())

df.loc[0:9,["MedInc","Population"]]


df.sort_values("Population").iloc[0:4,:]

df.groupby("AveRooms")["AveBedrms"].transform('sum')

df["total_quartos"] = df.groupby('AveRooms')["AveBedrms"].transform('sum')

df["Percent_of_Order"] = df["AveBedrms"] / df["AveRooms"]