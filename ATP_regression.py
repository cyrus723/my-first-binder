# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 15:26:53 2022

@author: hy11
"""

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from pylab import mpl, plt
#plt.style.use("fivethirtyeight")
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'arial'
mpl.rcParams["savefig.dpi"] = 700
np.set_printoptions(precision=5, suppress=True,
                    formatter={"float": lambda x: f"{x:6.3f}"})
%config InlineBackend.figure_format = 'jpg'


mypath = 'C:/Users/hy11/pyproj/sackmann/'


data = pd.read_excel(mypath + 'leader.xls')

data.head()

data

#%%

data.info()

#%%

formula = 'Rk ~ MWP + SPW + AceP +DFP + FirstinP + HldP + PtsSG '
results = smf.ols(formula, data).fit()
print(results.summary())

data2=data.sort_values(by=['Aces'], ascending = False)
data3=data2[['Player', 'Aces']]
print(data3)

import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots(figsize=(10,6))
plt.bar(data3["Player"], data3["Aces"], color ='blue',\
        width = 0.5)

plt.title('Most Aces by Top 50 Players since ????', size=16)
plt.ylabel("Aces", size=15)
#plt.xlabel("Players", size=15) 
plt.xticks(rotation = 85, size=17)
plt.tight_layout()
plt.show(    
)

#ax.set_ylabel(player_id"])

data2=data.sort_values(by=['FirstinP'], ascending=False)
data3=data2[['Player', 'FirstinP']]
print(data3)

fig, ax = plt.subplots(figsize=(10,6))
plt.bar(data3["Player"], data3["FirstinP"], color ='blue',\
        width = 0.5)

plt.title('Most First Serve-In Percentage of Top 50 Players since ????', size=15)
plt.ylabel("Aces", size=15)
#plt.xlabel("Players", size=15) 
plt.xticks(rotation = 85, size=17)
plt.tight_layout()
plt.show()