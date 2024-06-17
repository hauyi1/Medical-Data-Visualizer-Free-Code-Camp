import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = None

# 3
df['cholesterol'] = df['cholesterol'].map({1: 0, 2: 1, 3:1})
df['gluc'] = df['gluc'].map({1: 0, 2: 1, 3:1})

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol','gluc','smoke','alco','active','overweight'])
    

    # 6
    df_cat['count']=1
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).count()

    # 7

    catplot = sns.catplot(data=df_cat, x='variable', y='count', hue='value', col="cardio", kind='bar')

    # 8
    fig = catplot


    # 9
    fig.savefig('catplot.png')
    return fig
draw_cat_plot()

# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
