# -*- coding: utf-8 -*-
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
from sklearn.compose import ColumnTransformer
import pandas as pd
import numpy as np
import logging
from ..features.build_features import add_extra_features


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

    # Build pipelines
    # Numerical Pipelines
    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="median")),
        ('attribs_adder', FunctionTransformer(add_extra_features, validate=False)),
        ('std_scaler', StandardScaler()),
    ])

    # Now we can combine both pipelines numerical and categorical into one
    # columns for numerical data
    num_attribs = list(housing)
    num_attribs.remove("ocean_proximity")
    # column for categorical data
    cat_attribs = ["ocean_proximity"]

    full_pipeline = ColumnTransformer([
        ("num", num_pipeline, num_attribs),
        ("cat", OneHotEncoder(), cat_attribs),
    ])

    # Transorm data
    housing_prepared = full_pipeline.fit_transform(housing)

    # Save the transformed data and pipeline parameters
    joblib.dump(full_pipeline, 'models/full_pipeline.pkl')
    joblib.dump(housing_prepared, 'data/processed/'+'housing_prepared'+'.pkl')
    joblib.dump(housing_labels, 'data/processed/'+'housing_labels'+'.pkl')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()
