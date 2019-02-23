# -*- coding: utf-8 -*-
import logging
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit


def main():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    file_name = 'data/raw/housing.csv'
    housing_df = pd.read_csv(file_name)

    # Create income category
    # Divide by 1.5 to limit the number of income categories
    housing_df["income_cat"] = np.ceil(housing_df["median_income"] / 1.5)
    # Label those above 5 as 5
    housing_df["income_cat"].where(housing_df["income_cat"] < 5, 5.0, inplace=True)

    # split data again but this time with strata
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(housing_df, housing_df["income_cat"]):
        strat_train_set = housing_df.loc[train_index]
        strat_test_set = housing_df.loc[test_index]

    # Now we can drop the income cat column
    strat_train_set.drop("income_cat", axis=1, inplace=True)
    strat_test_set.drop("income_cat", axis=1, inplace=True)

    # drop labels for training set
    # here the drop method also creates a copy
    housing = strat_train_set.drop("median_house_value", axis=1)
    housing_labels = strat_train_set["median_house_value"].copy()

    # remove text data, cannot impute
    # create copy
    housing_num = housing.drop('ocean_proximity', axis=1)

    # get the right column indices: safer than hard-coding indices 3, 4, 5, 6
    rooms_ix, bedrooms_ix, population_ix, household_ix = [list(housing.columns).index(
        col) for col in ("total_rooms", "total_bedrooms", "population", "households")]

    print(rooms_ix, bedrooms_ix, population_ix, household_ix)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()
