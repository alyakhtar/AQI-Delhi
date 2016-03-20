import numpy as np
import pandas as pd
import cPickle as pickle
from math import sqrt
from pybrain.datasets.supervised import SupervisedDataSet as SDS
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain import *

output_model_file = 'model.pkl'

X = pd.read_csv('Train/Train_Combine.csv', usecols=[
                'T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM'])
Y = pd.read_csv('Train/Train_Combine.csv', usecols=['PM 2.5'])

X = X.values
Y = Y.values

hidden_size = 100
epochs = 600

input_size = X.shape[1]
target_size = Y.shape[1]

ds = SDS( input_size, target_size )
ds.setField( 'input', X )
ds.setField( 'target', Y )

net = buildNetwork( input_size, hidden_size, target_size, bias = True, hiddenclass=TanhLayer)
trainer = BackpropTrainer( net,ds )

print "training for {} epochs...".format( epochs )

for i in range( epochs ):
	mse = trainer.train()
	rmse = sqrt( mse )
	print "training RMSE, epoch {}: {}".format( i + 1, rmse )
	
pickle.dump( net, open( output_model_file, 'wb' ))






