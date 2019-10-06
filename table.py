import pandas as pd

df = pd.read_csv("Resources/cities.csv")
df = df.drop("Unnamed: 0", axis=1)
df.to_html("table.html", index=False)