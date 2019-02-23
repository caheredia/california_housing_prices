import numpy as np
import pandas as pd
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestRegressor

# This needs to be run from home director with -m switch,
# python -m src.models.cost_estimator

# Load model
full_pipeline = joblib.load('models/full_pipeline.pkl')
forest_reg = joblib.load("models/forest_model.pkl")

# columns for test data
columns = ['longitude',
           'latitude',
           'housing_median_age',
           'total_rooms',
           'total_bedrooms',
           'population',
           'households',
           'median_income',
           'ocean_proximity']

print('Enter house parameters:')
print('For example:\n longitude|latitude|housing_median_age|total_rooms|total_bedrooms|population|households|median_income|ocean_proximity')
print('As: -122.23,37.88,41.0,880.0,129.0,322.0,126.0,8.3252,"NEAR BAY"')
x = input().split(',')
# convert to arrray and format data for transform
data = []
for item in x:
    try:
        data.append(float(item))
    except:
        data.append(item[1:-1])
test = pd.DataFrame(data).T
test.columns = columns
x_prepared = full_pipeline.transform(test)
prediction = forest_reg.predict(x_prepared)
print('\n')
print('Estimate: ${:,}'.format(int(prediction)))
