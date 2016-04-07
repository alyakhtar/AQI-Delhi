from keras.models import Sequential, Graph
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
import pandas as pd
import time
import math
import matplotlib.pyplot as plt
from Confuse import main
from sklearn.metrics import mean_absolute_error
from keras.utils import np_utils


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

Y = np_utils.to_categorical(Y)
Y2 = np_utils.to_categorical(Y2)


model = Sequential()

model.add(Dense(10, input_dim=8, init='uniform'))
model.add(Activation('tanh'))
model.add(Dense(10, input_dim=10, init='uniform'))
model.add(Activation('tanh'))
model.add(Dense(6, input_dim=10, init='uniform'))
model.add(Activation('softmax'))

sgd = SGD(lr=0.1, decay=1e-3, momentum=0.5, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd)

model.fit(X, Y, nb_epoch=500, batch_size=1, show_accuracy=True)
score = model.evaluate(X2, Y2, batch_size=1)
preds = model.predict(X2, batch_size=1, verbose=0)

# print preds
# main(Y2, preds)

# plt.plot(xrange(0, 441), preds, label='Observed')
# plt.plot(xrange(0, 441), Y2, label='Expected')
# plt.xlabel('Data Points')
# plt.ylabel('PM 2.5')
# plt.legend(loc='upper right')
# plt.show()

print "Error : ", score
