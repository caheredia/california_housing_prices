from sklearn.externals import joblib
import logging
from sklearn.ensemble import RandomForestRegressor


def main():
    """ Trains model using processed data
        Saves model (saved in ../models).
    """
    logger = logging.getLogger(__name__)
    logger.info('traning model from processed data')

    # Load saved transformed data
    housing_prepared = joblib.load('data/processed/'+'housing_prepared'+'.pkl')
    housing_labels = joblib.load('data/processed/'+'housing_labels'+'.pkl')
    strat_test_set = joblib.load('data/processed/'+'strat_test_set'+'.pkl')

    # Train model
    forest_reg = RandomForestRegressor(n_estimators=30, max_features=8, random_state=42)
    forest_reg.fit(housing_prepared, housing_labels)

    # Save model
    joblib.dump(forest_reg, "models/forest_model.pkl", compress=True)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()
