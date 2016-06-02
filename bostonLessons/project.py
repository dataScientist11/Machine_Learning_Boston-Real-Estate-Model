##ANSWERS
#Q1 The three features that are most significant are CRIM, RM and DIS. CRIM measures per capita crime rate per town, RM measures average number of rooms per dwelling, and DIS measures weighted distance to 5 Boston employment centers. CRIM could demonstrate the socioeconomics of the region and would inadvertently signifiy housing values. Number of rooms (RM) could be a loose measure of how large the house is, which correlates with housing value. Distance to employment centers (DIS) could increase value of the house for occupants. 
#In [4] The corresponding client values for CRIM, RM and DIS in order are: 11.95, 5.609, and 1.385
#paraphrase: We separate training and testing sets so we can get a better idea whether the model can generalize to unseen data rather than fit to the data just seen.
#Splitting the data into training and testing subsets will allow the model to be tested for unseen data. Furthermore we can make evaluations on if the model {overfits or has high variance} or {if it is underfitted or has high bias}.
#The chosen performance metric was mean squared error. Graphical representations are often used. Also it is known to encompass both variance and bias. 
# Importing a few necessary libraries
# Importing a few necessary libraries
import numpy
import matplotlib.pyplot as pl
from sklearn import datasets
from sklearn.tree import DecisionTreeRegressor

# Make matplotlib show our plots inline (nicely formatted in the notebook)
%matplotlib inline

# Create our client's feature set for which we will be predicting a selling price
CLIENT_FEATURES = [[11.95, 0.00, 18.100, 0, 0.6590, 5.6090, 90.00, 1.385, 24, 680.0, 20.20, 332.09, 12.13]]

# Load the Boston Housing dataset into the city_data variable
city_data = datasets.load_boston()

# Initialize the housing prices and housing features
housing_prices = city_data.target
housing_features = city_data.data

print "Boston Housing dataset loaded successfully!"