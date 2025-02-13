# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nH0PSdHwzQwsQxTW1rEMntC0vXdtyqnj
"""

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from scipy.stats import pearsonr , spearmanr

#create linear data

data1 = {
    'x':[1,2,3,4,5,6,7,8,9,10], 'y':[2,4,6,8,10,12,14,16,18,20]
}

df1 = pd.DataFrame(data1)

df1

data2= {
    'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'y': [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
}

df2 = pd.DataFrame(data2)

df2

print(df2)

#calculations

pearson_corr = pearsonr(df1['x'], df1['y'])

spearman_corr = spearmanr(df2['x'], df2['y'])

pearson_corr

spearman_corr

plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.scatter(df1['x'], df2['y'],color = 'b', label = 'pearson correlation')
plt.plot(df1['x'], df1['y'], color = 'r', linestyle = '-')


plt.subplot(1,2,2)
plt.scatter(df2['x'], df2['y'],color = 'g', label = 'spearman correlation')
plt.plot(df2['x'], df2['y'], color = 'orange', linestyle = '-')

