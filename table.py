import pandas as pd

df = pd.read_csv("../HW/api_hw/output_data/cities.csv")
df.to_html("table.html")