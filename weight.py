import plotly.figure_factory as ff
import pandas as pd
df = pd.read_csv("HeightWeight.csv")
weightlist = df["Weight(Pounds)"]
fig = ff.create_distplot([weightlist],['weightresult'],show_hist = False)
fig.show()
