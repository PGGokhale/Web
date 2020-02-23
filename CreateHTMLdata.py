import os
import pandas as pd

filepath = os.path.join("Resources", "cities.csv")
filepath1 = os.path.join("data1.html")
df = pd.read_csv(filepath, index_col=False)
df.set_index('City_ID', inplace=True)

table = df.to_html()
with open(filepath1, "w") as f:
    f.write(table)