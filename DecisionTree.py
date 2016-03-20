import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_absolute_error
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

regr_1 = DecisionTreeRegressor(max_depth=5)
regr_1.fit(X, Y)


y_1 = regr_1.predict(X2)


print mean_absolute_error(Y2, y_1)

main(Y2,y_1)

# plt.figure()
# plt.scatter(Y, Y, c="k", label="data")
# plt.plot(Y2, y_1, c="g", label="max_depth=2", linewidth=2)
# # plt.plot(X_test, y_2, c="r", label="max_depth=5", linewidth=2)
# plt.xlabel("data")
# plt.ylabel("target")
# plt.title("Decision Tree Regression")
# plt.legend()
# plt.show()
