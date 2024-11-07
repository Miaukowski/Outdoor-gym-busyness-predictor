"""
Module for performing EDA on said dataframe, 
Bar plots and heatmap of the correlation matrix
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


def EDA(df: pd.DataFrame):
    """
    Plots a lot of plots for visualising relationships between variables. 
    Takes in the dataframe of interest. 
    """
    plt.figure(figsize=(10, 6))
    yearly_usage = df.groupby('year')['usage_mins_total (mins)'].mean()
    yearly_usage.plot(kind='bar')
    plt.title('Average Usage hourly per Year')
    plt.ylabel('Average usage hourly')
    plt.xlabel('Year')
    plt.show()


    plt.figure(figsize=(10, 6))
    monthly_usage = df.groupby('month')['usage_mins_total (mins)'].mean()
    monthly_usage.plot(kind='bar')
    plt.title('Average Usage hourly Minutes per Month')
    plt.ylabel('Average Usage hourly')
    plt.xlabel('Month')
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    plt.xticks(ticks=np.arange(12), labels=month_names, rotation=30)
    plt.show()


    plt.figure(figsize=(10, 6))
    day_usage = df.groupby('day')['usage_mins_total (mins)'].mean()
    day_usage.plot(kind='bar')
    plt.title('Average Usage Minutes hourly per Day of the Week')
    plt.ylabel('Average Usage Minutes hourly')
    plt.xlabel('Day of the Week')
    day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    plt.xticks(ticks=np.arange(7), labels=day_names, rotation=30)
    plt.show()


    plt.figure(figsize=(10, 6))
    hourly_usage = df.groupby('hour')['usage_mins_total (mins)'].mean()
    hourly_usage.plot(kind='bar')
    plt.title('Average Usage Minutes per Hour')
    plt.ylabel('Average Usage Minutes hourly')
    plt.xlabel('Hour')
    plt.xticks(ticks=np.arange(24))
    plt.show()

    corr_matrix = df.corr()
    sns.heatmap(corr_matrix)
    plt.show()


