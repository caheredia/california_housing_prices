import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


# get the right column indices: safer than hard-coding indices 3, 4, 5, 6
def get_indices(filename='data/raw/housing.csv'):
    """
    Retrieves incdices from selected columns. 

    Function loads the first row csv, then converts labels to list. 
    Finally retreives column index from name. 

    Parameters
    ----------
    filename : string (optional) 
        data location 

    Returns
    -------
    list
        list with indices

    """
    data = pd.read_csv(filename, nrows=0)
    columns = list(data)
    return [columns.index(col) for col in ("total_rooms", "total_bedrooms", "population", "households")]


def add_extra_features(X, add_bedrooms_per_room=True):
    '''Adds extra features to data sets.

    If boolean is true adds bedrooms per room column.
    Also adds rooms_per_household and population_per_household columns.

    Parameters
    ----------
    X : numpy.Array
        dataframe to modify
    column_name : string (optional)
        column containing hourly data


    Returns
    -------
    X : numpy.Array
        transformed array .
    '''

    rooms_ix, bedrooms_ix, population_ix, household_ix = get_indices()

    rooms_per_household = X[:, rooms_ix] / X[:, household_ix]
    population_per_household = X[:, population_ix] / X[:, household_ix]
    if add_bedrooms_per_room:
        bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
        return np.c_[X, rooms_per_household, population_per_household,
                     bedrooms_per_room]
    else:
        return np.c_[X, rooms_per_household, population_per_household]

def save(items, location='data/processed/'):
    """
    Saves the variables in items to pickles. 

    Prints the variable name and save location

    Parameters
    ----------
    items : list
       strings of variable names 
    location : string (optional)
        directory location for save 


    Returns
    -------
    None
    """
    for item in items:
        # full save name
        filename = location + item + '.pkl'
        # save to pickle
        joblib.dump(eval(item), filename)
        print(filename)