from pandas import DataFrame, read_csv

import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number


print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)


df = pd.read_csv(filepath_or_buffer="data/GL2010.txt", header=None)

print("SIZE: " + str(df.size) + " COLUMNS: " + str(df.columns) + "\n")

print("Visiting teams!: \n" + str(df[3].unique()) + "\n")