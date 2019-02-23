import numpy as np
import pandas as pd
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestRegressor

# This needs to be run from home director with -m switch, 
# python -m src.models.cost_estimator

# Load model
full_pipeline = joblib.load('models/full_pipeline.pkl')
forest_reg = joblib.load("models/forest_model.pkl")

print(forest_reg)
