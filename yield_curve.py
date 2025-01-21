# -*- coding: utf-8 -*-
"""Yield Curve.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/129NPKWiIrNRZnOHYJKsCDXroDrYeGng1
"""

!pip install --quiet fredapi

import pandas as pd
import numpy as np
import matplotlib.animation as animation
from IPython.display import HTML
from fredapi import Fred

API_KEY = 'oops you need to put your own lol'
fred = Fred(api_key=API_KEY)

series_ids = {
    '1 Mo': 'DGS1MO',
    '3 Mo': 'DGS3MO',
    '6 Mo': 'DGS6MO',
    '1 Yr': 'DGS1',
    '2 Yr': 'DGS2',
    '5 Yr': 'DGS5',
    '10 Yr': 'DGS10',
    '30 Yr': 'DGS30'
}

df = pd.DataFrame()
for label, sid in series_ids.items():
  df[label]= fred.get_series(sid)

df = df.loc["1995":"2024"]
df = df.resample("M").first()
df.dropna(inplace=True)

fig, ax = plt.subplots(figsize=(8, 5))
maturities = df.columns.tolist()

def animate(i):
    ax.clear()
    date = df.index[i]
    values = df.iloc[i].values

    # Plot yields for this date
    ax.plot(maturities, values, marker='o')

    # Titles and labels
    ax.set_title(str(date.date()))
    ax.set_xlabel("Maturity")
    ax.set_ylabel("Yield (%)")

    # Keep a consistent y-axis range
    ax.set_ylim(0, df.max().max() + 1)

ani = animation.FuncAnimation(fig, animate, frames=len(df), interval=200)

# 7. Display the animation inline in Colab
HTML(ani.to_jshtml())
