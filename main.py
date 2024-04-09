# This entrypoint file to be used in development. Start by reading README.md
#import sea_level_predictor
#from unittest import main

# Test your function by calling it here
#sea_level_predictor.draw_plot()

# Run unit tests automatically
#main(module='test_module', exit=False)


#----my code starts here-----
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

#import data from file
df = pd.read_csv("epa-sea-level.csv")

fig, ax = plt.subplots(figsize=(8,8))
scatter = plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

fig.savefig('scatter.png')


#print(df.head())