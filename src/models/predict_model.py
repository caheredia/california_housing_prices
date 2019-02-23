import numpy as np
import pandas as pd
from sklearn.externals import joblib
import logging
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


def main():
    """ Makes predictions using saved models
        (saved in ../models).
    """
    logger = logging.getLogger(__name__)
    logger.info('predicting values')

    # Load data
    strat_test_set = joblib.load('data/processed/'+'strat_test_set'+'.pkl')

    # Load model
    full_pipeline = joblib.load('models/full_pipeline.pkl')
    forest_reg = joblib.load("models/forest_model.pkl")

    # Evaluate test data
    final_model = forest_reg
    X_test = strat_test_set.drop("median_house_value", axis=1)
    y_test = strat_test_set["median_house_value"].copy()

    X_test_prepared = full_pipeline.transform(X_test)
    final_predictions = final_model.predict(X_test_prepared)

    final_mse = mean_squared_error(y_test, final_predictions)
    final_rmse = np.sqrt(final_mse)

    print('final rmse: \t {}'.format(int(final_rmse)))
    print('model score: \t {:.1%}'.format(final_model.score(X_test_prepared, y_test)))


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()
