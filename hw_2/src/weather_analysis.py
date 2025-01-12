"""Weather Analysis Exercise"""
import pandas as pd
import matplotlib.pyplot as plt

"""
Exercise 3: Weather Data Analysis with Pandas
------------------------------------------
Task: Analyze temperature and precipitation patterns.

Required steps:
1. Calculate basic statistics:
   - Monthly temperature averages
   - Total precipitation by month
   - Seasonal patterns
   - Temperature-precipitation correlation

2. Create seasonal analysis:
   - Group data by seasons
   - Calculate seasonal averages
   - Identify extreme weather months

3. Create visualizations:
   - Dual-axis plot for temperature and precipitation
   - Seasonal temperature averages
   - Temperature distribution
   - Temperature vs precipitation scatter plot

Parameters:
-----------
df : pandas.DataFrame
    DataFrame with columns:
    - Month: month names
    - Temperature: temperature values in Celsius
    - Precipitation: precipitation values in mm

Expected Output:
--------------
1. Four-panel figure showing:
   - Temperature and precipitation trends
   - Seasonal averages
   - Temperature distribution
   - Correlation scatter plot
2. Dictionary with weather statistics

Hint: Use pd.cut for seasonal grouping
"""


def analyze_weather(df):
    #calcoli base
    monthly_temp_averages = df.groupby('Month')['Temperature'].mean()  #prendo il df e calc della media mensile
    total_precipitation_by_month = df.groupby('Month')['Precipitation'].sum()  #calcolo la somma delle prec mensile

    #calcolo la correlazione
    correlation = df['Temperature'].corr(df['Precipitation'])

    #creo il dizionario per definire le stagioni
    seasons = {
        'Winter': ['Dec', 'Jan', 'Feb'],
        'Spring': ['Mar', 'Apr', 'May'],
        'Summer': ['Jun', 'Jul', 'Aug'],
        'Autumn': ['Sep', 'Oct', 'Nov']
    }
    #dict comprehension, itero per ogni coppia key-value calcolo media temp e somma prec
    seasonal_averages = {
        season: {
            'Average Temperature': monthly_temp_averages[months].mean(),
            'Total Precipitation': total_precipitation_by_month[months].sum()
        }
        for season, months in seasons.items()
    }
    #vado a creare dizionari per i mesi con temp estreme
    extreme_temp_months = {
        'Hottest': df.loc[df['Temperature'] == df['Temperature'].max(), 'Month'].values[0],
        'Coldest': df.loc[df['Temperature'] == df['Temperature'].min(), 'Month'].values[0]
    }

    extreme_prec_months = {
        'Wettest': df.loc[df['Precipitation'] == df['Precipitation'].max(), 'Month'].values[0],
        'Driest': df.loc[df['Precipitation'] == df['Precipitation'].min(), 'Month'].values[0]
    }



    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

    #plot1
    axes[0, 0].plot(monthly_temp_averages.index, monthly_temp_averages, label='Temperature')
    axes[0, 0].bar(total_precipitation_by_month.index, total_precipitation_by_month, alpha=0.7, label='Precipitation')
    axes[0, 0].set_xlabel('Month')
    axes[0, 0].set_ylabel('Values')
    axes[0, 0].set_title('Temperature and Precipitation Trends')
    axes[0, 0].legend()

    #plot2
    seasonal_temp_averages = [seasonal_averages[season]['Average Temperature'] for season in seasons]
    seasonal_prec_averages = [seasonal_averages[season]['Total Precipitation'] for season in seasons]
    axes[0, 1].bar(seasons.keys(), seasonal_temp_averages, label='Temperature')
    axes[0, 1].set_xlabel('Season')
    axes[0, 1].set_ylabel('Average Temperature')
    axes[0, 1].set_title('Seasonal Temperature Averages')

    #plot3
    axes[1, 0].hist(df['Temperature'], bins=20)
    axes[1, 0].set_xlabel('Temperature')
    axes[1, 0].set_ylabel('Frequency')
    axes[1, 0].set_title('Temperature Distribution')

    #plot4
    axes[1, 1].scatter(df['Temperature'], df['Precipitation'])
    axes[1, 1].set_xlabel('Temperature')
    axes[1, 1].set_ylabel('Precipitation')
    axes[1, 1].set_title('Temperature vs Precipitation')

    #plt.tight_layout()
    plt.show()
    pass





