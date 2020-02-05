"""

Run Configurations (Automatically created with right-click)

 - Run
 - Debug
 - DataViewer in Debugger

"""
from random import randint

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor


def get_features_targets(data):
    features = np.zeros((data.shape[0], 4))
    features[:, 0] = data['u'] - data['g']
    features[:, 1] = data['g'] - data['r']
    features[:, 2] = data['r'] - data['i']
    features[:, 3] = data['i'] - data['z']

    return features, data['redshift']


def train_model(feat, targs):
    # initialize model
    dtr = DecisionTreeRegressor()
    # train the model
    dtr.fit(feat, targs)
    # make predictions using the same features
    predictions = dtr.predict(feat)
    return predictions


def generate_df():
    size = 50
    max_val = 100
    generated_df = pd.DataFrame({'row': [randint(0, max_val) for _ in range(size)],
                                 'A': [randint(0, max_val) for _ in range(size)],
                                 'B': [randint(0, max_val) for _ in range(size)],
                                 'C': [randint(0, max_val) for _ in range(size)],
                                 'D': [randint(0, max_val) for _ in range(size)]})
    return generated_df


loaded_data = np.load('../data/sdss_galaxy_colors.npy')
features, targets = get_features_targets(loaded_data)
random_df = generate_df()

predicts = train_model(features, targets)  # breakpoint

# print out the first 4 predicted redshifts
print(predicts[:4])
