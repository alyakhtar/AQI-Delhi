from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
import pandas as pd
import time

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

model = Sequential()
# Dense(64) is a fully-connected layer with 64 hidden units.
# in the first layer, you must specify the expected input data shape:
# here, 20-dimensional vectors.
model.add(Dense(10, input_dim=8, init='uniform'))
model.add(Activation('tanh'))
model.add(Dense(10,input_dim=10, init='uniform'))
model.add(Activation('tanh'))
model.add(Dense(1,input_dim=10, init='uniform'))
model.add(Activation('tanh'))

sgd = SGD(lr=0.1, decay=1e-3, momentum=0.5, nesterov=True)
model.compile(loss='mean_squared_error',
              optimizer=sgd)

model.fit(X, Y,
          nb_epoch=20,
          batch_size=1,
          show_accuracy=True)
score = model.evaluate(X2, Y2, batch_size=1)
preds = model.predict(X2, batch_size=1, verbose=0)


print "Error: ",score*100
print "Accuracy: ", (1-score)*100
# time.sleep(2)
print preds[:10],Y2[:10]
