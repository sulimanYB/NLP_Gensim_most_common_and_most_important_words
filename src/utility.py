import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB 

import seaborn as sns
import matplotlib.pyplot as plt

def plot_words(df, x, y, title):
    """
    This function plots accuracy at different alpha values.
    Inputs:
        - df: dataframe
        - x: the column name (x-axis)
        - y: the column name (y-axis) 
        - title: The graph title
    """
    g = sns.set_theme(style="white")
    sns.barplot(x=x, y=y, data=df).set_title(title, fontsize=16)
    plt.xticks(rotation=70)
    sns.despine(right=True, top=True)
    plt.show()