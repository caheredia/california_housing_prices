import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


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
    data : pandas.DataFrame
        Original dataframe with Chicago crime time stamps as DateTimeIndex.
    '''

    rooms_per_household = X[:, rooms_ix] / X[:, household_ix]
    population_per_household = X[:, population_ix] / X[:, household_ix]
    if add_bedrooms_per_room:
        bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
        return np.c_[X, rooms_per_household, population_per_household,
                     bedrooms_per_room]
    else:
        return np.c_[X, rooms_per_household, population_per_household]
