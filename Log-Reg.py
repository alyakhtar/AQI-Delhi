from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor, NearestNeighbors
import pandas as pd
import numpy as np
from sklearn import metrics

X = pd.read_csv('Train/Train_Combine.csv', usecols=[
                'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM'])
Y = pd.read_csv('Train/Train_Combine.csv', usecols=['PM 2.5'])

X = X.values
Y = Y.values
# Y = np.asarray(Y,dtype="|S6")

X2 = pd.read_csv('Test/Test_Combine.csv', usecols=[
                 'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM'])
Y2 = pd.read_csv('Test/Test_Combine.csv', usecols=['PM 2.5'])

X2 = X2.values
Y2 = Y2.values

abc = SVR(kernel='rbf')
abc.fit(X, Y)
# KNeighborsRegressor(algorithm='auto', leaf_size=30, weights='uniform')
# print w

# for i in xrange(X2.shape[0]):
# print knn.predict(X2[0])[0], Y[0]
# print metrics.mean_absolute_error(Y2, knn.predict(X2))

err = metrics.mean_absolute_error(Y2, abc.predict(X2)) *100
print ("Mean Absolute Error: %f" % err)  # evaluate performance
print ("Accuracy: %f" % (100 - err))
# print nn.kneighbors(X2[0])[0], Y[0]
# break
