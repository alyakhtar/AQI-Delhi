import numpy as np
import cPickle as pickle
import pandas as pd
from math import sqrt
from pybrain.datasets.supervised import SupervisedDataSet as SDS
from sklearn.metrics import mean_squared_error as MSE
from Confuse import main

model_file = 'model.pkl'
output_predictions_file = 'predictions.txt'

X2 = pd.read_csv('Test/Test_Combine.csv', usecols=[
                 'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM'])
Y2 = pd.read_csv('Test/Test_Combine.csv', usecols=['PM 2.5'])

X2 = X2.values
Y2 = Y2.values
net = pickle.load( open( model_file, 'rb' ))

y_test_dummy = np.zeros( Y2.shape )

input_size = X2.shape[1]
target_size = X2.shape[1]

ds = SDS( input_size, target_size )
ds.setField( 'input', X2 )
ds.setField( 'target', y_test_dummy )

p = net.activateOnDataset( ds )
	
mse = MSE( Y2, p )
rmse = sqrt( mse )

print "testing RMSE:", rmse
print "testing MSE: ", mse

main(Y2,p)
np.savetxt( output_predictions_file, p, fmt = '%.6f' )
