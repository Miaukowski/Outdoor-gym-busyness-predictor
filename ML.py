"""
The random forest function for modeling, 
as well as the predictor for later.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def rand_forrest(df: pd.DataFrame) -> tuple[float,RandomForestRegressor]:
    """
    Trains the data using RandomForest regression. 
    Splits the data into train and test batches.
    Returns a tuple containing the R² score, and the model. 

    """
    X = df.drop(columns=['usage_mins_total (mins)', 'utctimestamp'])
    Y = df['usage_mins_total (mins)']
    x_train, x_test , y_train, y_test = train_test_split(X,Y, train_size=0.3,random_state=42)

    regr = RandomForestRegressor(n_estimators=300, random_state=42)
    regr.fit(x_train, y_train)
    return regr.score(x_test,y_test), regr


def predictor(regr: RandomForestRegressor, df: pd.DataFrame)-> pd.DataFrame:
    """
    Uses the model trained in the function rand_forrest, to predict
    the number of usage minutes.
    """
    df['predicted_usage_minutes'] = regr.predict(df)
    return df

