import plotly.figure_factory as ff
import pandas as pd 
df = pd.read_csv("HeightWeight.csv")
heightlist = df["Height(Inches)"].tolist()
fig = ff.create_distplot([heightlist],['Heightresult'],show_hist = False)
fig.show()
