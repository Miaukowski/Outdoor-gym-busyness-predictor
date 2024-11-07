"""
Module for the final plots. 
"""

import calendar
import matplotlib.pyplot as plt 
import pandas as pd

#Here we simply plot the result for the visualtisations going to the blogpost for the user. 



def plotting_charts(df: pd.DataFrame, month_int: int, area: str):
    """
    For generating plots for each months (weekdays & hourly) for hourly usage minutes. 
    """
    month = df[df['month'] == month_int]
    month_area = month[month[area] == 1]
    
    plt.figure(figsize=(10, 6))

    daily_data = month_area.groupby('day').agg({
        'predicted_usage_minutes': 'mean',
        'Average temperature [°C]': 'mean'
    }).reset_index()


    ax = daily_data.plot(
        x='day', 
        y='predicted_usage_minutes', 
        kind='bar', 
        legend=False, 
        ax=plt.gca(), 
        color='#C79FEF'
    )
    ax.set_ylabel('Hourly Usage Minutes', fontsize=12)
    ax.set_xlabel('Day of Week', fontsize=12)
    ax.tick_params(axis='both', labelsize=10)
    ax.set_ylim(0,10)


    ax2 = ax.twinx()
    daily_data.plot(
        x='day', 
        y='Average temperature [°C]', 
        ax=ax2, 
        color='black', 
        kind='line', 
        legend=False
    )
    ax2.set_ylabel('Average Temperature [°C]', fontsize=12)
    ax2.tick_params(axis='y', labelsize=10)
    ax.legend(['Hourly Usage Minutes'], loc='upper left', bbox_to_anchor=(1.1, 1), fontsize=10)
    ax2.legend(['Average Temperature'], loc='upper left', bbox_to_anchor=(1.1, 0.9), fontsize=10)
    plt.title(f'Average machine usage minutes per hour by weekday in {calendar.month_name[month_int]} in {area}', fontsize=14)
    plt.tight_layout()
    plt.savefig(f'{area}_plots/{calendar.month_name[month_int]}_daily.png')



    plt.figure(figsize=(10, 6))


    hourly_data = month_area.groupby('hour').agg({
        'predicted_usage_minutes': 'mean',
        'Average temperature [°C]': 'mean'
    }).reset_index()


    ax = hourly_data.plot(
        x='hour', 
        y='predicted_usage_minutes', 
        kind='bar', 
        legend=False, 
        ax=plt.gca(), 
        color='#C875C4'
    )
    ax.set_ylabel('Hourly Usage Minutes', fontsize=12)
    ax.set_xlabel('Hour of Day', fontsize=12)
    ax.tick_params(axis='both', labelsize=10)
    ax.set_ylim(0,25)

    ax2 = ax.twinx()
    hourly_data.plot(
        x='hour', 
        y='Average temperature [°C]', 
        ax=ax2, 
        color='black', 
        kind='line', 
        legend=False
    )
    ax2.set_ylabel('Average Temperature [°C]', fontsize=12)
    ax2.tick_params(axis='y', labelsize=10)
    ax.legend(['Hourly Usage Minutes'], loc='upper left', bbox_to_anchor=(1.1, 1), fontsize=10)
    ax2.legend(['Average Temperature'], loc='upper left', bbox_to_anchor=(1.1, 0.9), fontsize=10)
    plt.title(f'Average machine usage minutes per hour in {calendar.month_name[month_int]} in {area}', fontsize=14)
    plt.tight_layout()
    plt.savefig(f'{area}_plots/{calendar.month_name[month_int]}_hourly.png')



def year_plot(df: pd.DataFrame, area: str):
    """
    Generates plots for each area over the whole year on hourly usage minutes. 
    """
    plt.figure(figsize=(10, 6))
    df = df[df[area] == 1]
    yearly_data =df.groupby('month').agg({
        'predicted_usage_minutes': 'mean',
        'Average temperature [°C]': 'mean'
    }).reset_index()


    ax = yearly_data.plot(
        x='month', 
        y='predicted_usage_minutes', 
        kind='bar', 
        legend=False, 
        ax=plt.gca(), 
        color='#C79FEF'
    )
    ax.set_ylabel('Hourly Usage Minutes', fontsize=12)
    ax.set_xlabel('Month', fontsize=12)
    ax.tick_params(axis='both', labelsize=10)
    ax.set_ylim(0,15)


    ax2 = ax.twinx()
    yearly_data.plot(
        x='month', 
        y='Average temperature [°C]', 
        ax=ax2, 
        color='black', 
        kind='line', 
        legend=False
    )
    ax2.set_ylabel('Average Temperature [°C]', fontsize=12)
    ax2.tick_params(axis='y', labelsize=10)
    ax.legend(['Hourly Usage Minutes'], loc='upper left', bbox_to_anchor=(1.1, 1), fontsize=10)
    ax2.legend(['Average Temperature'], loc='upper left', bbox_to_anchor=(1.1, 0.9), fontsize=10)
    plt.title(f'Average machine usage minutes per hour by month in {area}', fontsize=14)
    plt.tight_layout()
    plt.savefig(f'{area}_plots/year_daily.png')
    plt.figure(figsize=(10, 6))