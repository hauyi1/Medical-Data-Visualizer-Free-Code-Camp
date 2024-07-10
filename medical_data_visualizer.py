import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25)
df['overweight'] = df['overweight'].map({True: 1, False: 0})

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
    catplot.set_axis_labels('variable', 'total')


    # 8
    fig = catplot.fig
    

    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    lower_quantile_height = df['height'].quantile(0.025)
    upper_quantile_height = df['height'].quantile(0.975)
    lower_quantile_weight = df['weight'].quantile(0.025)
    upper_quantile_weight = df['weight'].quantile(0.975)

    # 11
    df_heat = df[(df['height'] >= lower_quantile_height) &
                (df['height'] <= upper_quantile_height) & 
                (df['weight'] >= lower_quantile_weight) & 
                (df['weight'] <= upper_quantile_weight)]

    # 12
    corr = df_heat.corr(numeric_only=False)


    # 13
    mask = np.triu(np.ones(corr.shape)).astype(bool)



    # 14
    fig, ax = plt.subplots(figsize=(10, 8))


    # 15 
    sns.heatmap(corr, mask=mask, annot=True, ax=ax, fmt="0.1f")
    plt.show()



    # 16
    fig.savefig('heatmap.png')
    return fig
