"""
Separated some functions here, they were used quite alot during the progress
of making this program, but alot was scrapped/changed in the end, kept some for
nostalgia. Did not feel like cluttering the main script with this. 
"""
import pandas as pd

def cleaner(df_1: pd.DataFrame)-> pd.DataFrame:
    """
    Cleans up the main dataframe (hourly gym data) given as a parameter. Adds columns for
    hour, month,year,day, season and creates binary columns is_weekend and 
    is_night. Returns the dataframe with these added columns. 
    """
    df = df_1.copy()
    df['hour'] = df['utctimestamp'].dt.hour
    df['month'] = df['utctimestamp'].dt.month
    df['year'] = df['utctimestamp'].dt.year
    df['day'] = df['utctimestamp'].dt.dayofweek  # 0=Monday, 6=Sunday
    df['season'] = df['utctimestamp'].apply(lambda x: (x.month % 12 + 3) // 3)  # Winter=1, Spring=2, etc.
    df['is_weekend'] = (df['utctimestamp'].dt.dayofweek > 4).astype(int)
    df['is_night'] = ((df['utctimestamp'].dt.hour > 22) | (df['utctimestamp'].dt.hour < 5)).astype(int)

    return df

def cleaner_weather (df_2: pd.DataFrame) -> pd.DataFrame:
    """
    For simply adding columns for hour, day, month and year to the
    weather DataFrame. Returns the dataframe. 
    """
    df = df_2.copy()
    df['hour'] = df['utctimestamp'].dt.hour
    df['month'] = df['utctimestamp'].dt.month
    df['year'] = df['utctimestamp'].dt.year
    df['day'] = df['utctimestamp'].dt.dayofweek  # 0=Monday, 6=Sunday

    return df


def fetch_machine_names(df: pd.DataFrame, area: str) -> list[str]:
    """
    Maps groupId to an actual machine name. 
    """
    #Some machines unfortunately not available from even the companys website
    mapping = {
        'OG10' : 'Squat',
        'OG23' : 'Low Row',
        'OG24' : 'Lat Pulldown',
        'OG30' : 'Bench Press',
        'OG31' : 'Incline Bench Press',
        'OG41' : 'Front Press',
        'OGFA41' : 'Free Access Front Press',
        'OG70' : 'Biceps Curl',
        'OG80' : 'Triceps Press',
        'OGFA24': 'Free Access Lat Pulldown',
        'OG26' : 'Seated Back Extension',
        'OG92' : 'Abdominal Machine',
        'OG12' : 'Multi Lift',
        'OG72' : 'Seated Biceps Curl',
        'OG22' : 'Seated Row',
        'OG85' : 'Seated Dip',
        'OG82' : 'Seated Triceps Press',
        'OG14' : 'Leg Press'
    }
    
    filtered_df = df[df['area'] == area]
    names = [mapping[groupId] for groupId in filtered_df['groupId'].str.upper().unique() if groupId in mapping]
    
    return names


