from keras.models import Sequential, Graph
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
import pandas as pd
import time
import math
import matplotlib.pyplot as plt
import numpy
from Confuse import main
from sklearn.metrics import mean_absolute_error
from keras.utils import np_utils
from scipy.stats.stats import pearsonr


X = pd.read_csv('Data/Train/Train_Combine.csv', usecols=[
                'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM'])
Y = pd.read_csv('Data/Train/Train_Combine.csv', usecols=['PM 2.5'])

X = X.values
Y = Y.values

X2 = pd.read_csv('Data/Test/Test_Combine.csv', usecols=[
                 'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM'])
Y2 = pd.read_csv('Data/Test/Test_Combine.csv', usecols=['PM 2.5'])

X2 = X2.values
Y2 = Y2.values

Y = np_utils.to_categorical(Y)
Y3 = np_utils.to_categorical(Y2)


model = Sequential()

model.add(Dense(10, input_dim=8, init='uniform'))
model.add(Activation('tanh'))
model.add(Dense(10, input_dim=10, init='uniform'))
model.add(Activation('tanh'))
model.add(Dense(10, input_dim=10, init='uniform'))
model.add(Activation('tanh'))
model.add(Dense(2, input_dim=10, init='uniform'))
model.add(Activation('softmax'))

sgd = SGD(lr=0.5, decay=1e-2, momentum=0.6, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd)

model.fit(X, Y, nb_epoch=20, batch_size=1, show_accuracy=True)
score = model.evaluate(X2, Y3, batch_size=1)
preds = model.predict(X2, batch_size=1, verbose=0)

main(Y2, preds)

print "Error : ", score
