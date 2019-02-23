import numpy as np
import pandas as pd


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
    # get the right column indices: safer than hard-coding indices 3, 4, 5, 6
    rooms_ix, bedrooms_ix, population_ix, household_ix = [list(housing.columns).index(
        col) for col in ("total_rooms", "total_bedrooms", "population", "households")]

    rooms_per_household = X[:, rooms_ix] / X[:, household_ix]
    population_per_household = X[:, population_ix] / X[:, household_ix]
    if add_bedrooms_per_room:
        bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
        return np.c_[X, rooms_per_household, population_per_household,
                     bedrooms_per_room]
    else:
        return np.c_[X, rooms_per_household, population_per_household]
