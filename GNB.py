import numpy as np
from sklearn.naive_bayes import GaussianNB
import pandas as pd
from sklearn import linear_model
from sklearn import datasets
from sklearn import metrics


X = pd.read_csv('Train/Train_Combine.csv', usecols=[
                'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM'])
y = pd.read_csv('Train/Train_Combine.csv', usecols=['PM 2.5'])

X = np.array(X)
y = np.array(y)

lin = linear_model.LinearRegression()  # initialize regressor

lin.fit(X, y)  # fit training data

X2 = pd.read_csv('Test/Test_Combine.csv', usecols=[
                 'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM'])
Y2 = pd.read_csv('Test/Test_Combine.csv', usecols=['PM 2.5'])

X2 = X2.values
Y2 = Y2.values

preds = lin.predict(X2)  # make prediction on X test set

print preds[0], Y2[0]
# print preds

print metrics.mean_absolute_error(Y2, preds)  # evaluate performance
# print y
# clf = GaussianNB()
# clf.fit(X, y)
# GaussianNB()


# print clf.predict([[0.3354632588,-0.5894590846]])
