"""Traffic Analysis Exercise""" 
import pandas as pd 
import matplotlib.pyplot as plt 


def analyze_traffic(df):
    """
    Exercise 4: Website Traffic Analysis with Pandas
    --------------------------------------------
    Task: Analyze website traffic patterns and bounce rates.
    
    Required steps:
    1. Time series analysis:
       - Calculate daily traffic patterns
       - Compute moving averages (3-day and 7-day)
       - Identify weekly patterns
    
    2. Bounce rate analysis:
       - Calculate average bounce rates
       - Correlate bounce rates with traffic
       - Identify high/low bounce rate periods
    
    3. Create visualizations:
       - Traffic trends with moving averages
       - Daily traffic patterns
       - Bounce rate trends
       - Traffic vs bounce rate correlation
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame with columns:
        - Date: datetime index
        - Visitors: daily visitor count
        - Bounce_Rate: daily bounce rate percentage
    
    Expected Output:
    --------------
    1. Four-panel figure showing:
       - Traffic trends with moving averages
       - Average daily traffic patterns
       - Bounce rate trend
       - Correlation scatter plot
    2. Dictionary with traffic statistics
    
    Hint: Use df.rolling for moving averages
    """
    #cast della data e set dell'indice del df
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df.set_index('Date', inplace=True)
    #calcolo le medie mobili, creo un dataframe nuovo
    df_moving_averages = pd.DataFrame()
    df_moving_averages['Visitors'] = df['Visitors'].copy()
    df_moving_averages['3-day_avg'] = df_moving_averages['Visitors'].rolling(window=3).mean()
    df_moving_averages['7-day_avg'] = df_moving_averages['Visitors'].rolling(window=7).mean()
    #faccio lo stesso anche per l'analisi giornaliera
    df_daily_traffic = df.groupby(df.index.dayofweek)['Visitors'].mean().reset_index()
    df_daily_traffic.columns = ['Day_of_Week', 'Average_Daily_Visitors']
    #plots
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))
    axs[0, 0].plot(df_moving_averages.index, df_moving_averages['Visitors'], label='Daily Visitors')
    axs[0, 0].plot(df_moving_averages.index, df_moving_averages['3-day_avg'], label='3-day Moving Average')
    axs[0, 0].plot(df_moving_averages.index, df_moving_averages['7-day_avg'], label='7-day Moving Average')
    axs[0, 0].set_xlabel('Date')
    axs[0, 0].set_ylabel('Number of Visitors')
    axs[0, 0].set_title('Traffic Trend with Moving Averages')
    axs[0, 0].legend()

    # Average daily traffic
    axs[0, 1].bar(df_daily_traffic['Day_of_Week'], df_daily_traffic['Average_Daily_Visitors'])
    axs[0, 1].set_xlabel('Day of Week')
    axs[0, 1].set_ylabel('Average Number of Visitors')
    axs[0, 1].set_title('Average Daily Traffic')
    axs[0, 1].set_xticks(range(7))
    axs[0, 1].set_xticklabels(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

    # Bounce rate trend
    axs[1, 0].plot(df['Bounce_Rate'])
    axs[1, 0].set_xlabel('Date')
    axs[1, 0].set_ylabel('Bounce Rate (%)')
    axs[1, 0].set_title('Bounce Rate Trend')

    # Traffic vs bounce rate correlation
    axs[1, 1].scatter(df['Visitors'], df['Bounce_Rate'])
    axs[1, 1].set_xlabel('Number of Visitors')
    axs[1, 1].set_ylabel('Bounce Rate (%)')
    axs[1, 1].set_title('Correlation Between Traffic and Bounce Rate')
    plt.show()
    pass
