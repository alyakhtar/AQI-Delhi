from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
from sklearn import metrics
from Confuse import main

X = pd.read_csv('Train/Train_Combine.csv', usecols=[
                'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM'])
Y = pd.read_csv('Train/Train_Combine.csv', usecols=['PM 2.5'])

X = X.values
Y = Y.values

X2 = pd.read_csv('Test/Test_Combine.csv', usecols=[
                 'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM'])
Y2 = pd.read_csv('Test/Test_Combine.csv', usecols=['PM 2.5'])

X2 = X2.values
Y2 = Y2.values

abc = RandomForestRegressor(n_estimators=10)
abc.fit(X, Y)

err = metrics.mean_absolute_error(Y2, abc.predict(X2)) * 100
print ("Mean Absolute Error: %f" % err)
main(Y2, abc.predict(X2))
