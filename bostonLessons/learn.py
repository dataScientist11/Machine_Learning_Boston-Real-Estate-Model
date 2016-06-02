# Importing a few necessary libraries
import numpy as np
import matplotlib.pyplot as pl
from sklearn import datasets
from sklearn.tree import DecisionTreeRegressor

# Create our client's feature set for which we will be predicting a selling price
CLIENT_FEATURES = [[11.95, 0.00, 18.100, 0, 0.6590, 5.6090, 90.00, 1.385, 24, 680.0, 20.20, 332.09, 12.13]]

# Load the Boston Housing dataset into the city_data variable
city_data = datasets.load_boston()

# Initialize the housing prices and housing features
housing_prices = city_data.target
housing_features = city_data.data
from numpy import array
from sklearn import cross_validation
import numpy as np 
total_houses = len(housing_prices)
def shuffle_split_data(X, y):
    """ Shuffles and splits data into 70% training and 30% testing subsets,
        then returns the training and testing subsets. """
    X_train = []
    y_train=[]
    X_test=[]
    y_test=[]
    rs = cross_validation.ShuffleSplit(total_houses, n_iter=1,test_size=.3, random_state=0)
    for train, test in rs:
        
        for val in train:
            X_train.append(X[val])
            y_train.append(y[val])
            
        for val in test:
            X_test.append(X[val])
            y_test.append(y[val])
    # Return the training and testing data subsets
    np_X_train = array(X_train)
    np_y_train = array(y_train)
    np_X_test = array(X_test)
    np_y_test = array(y_test)
    return np_X_train, np_y_train, np_X_test, np_y_test
# Test shuffle_split_data
try:
    X_train, y_train, X_test, y_test = shuffle_split_data(housing_features, housing_prices)
    print "Successfully shuffled and split the data!"
except:
    print "Something went wrong with shuffling and splitting the data."
