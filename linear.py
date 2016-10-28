import csv
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

dates = []
prices = []

def get_data(filename):
	with open(filename, 'r') as csvfile:
		csvFileReader = csv.reader(csvfile)
		next(csvFileReader) # skipping column names
		for row in csvFileReader:
			dates.append(int(row[0].split('-')[0]))
			prices.append(float(row[1]))
	return

def predict_price(dates, prices, x):
	dates = np.reshape(dates, (len(dates),1)) # converting to matrix of n X 1
	prices = np.reshape(prices, (len(prices),1))
	
	linear_mod = linear_model.LinearRegression() # defining the linear regression model
	linear_mod.fit(dates, prices) # fitting the data points in the model
	
	plt.scatter(dates, prices, color= 'black', label= 'Data') # plotting the initial datapoints 
	plt.plot(dates, linear_mod.predict(dates), color= 'red', label= 'Linear model') # plotting the line made by linear regression
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.title('Linear Regression')
	plt.legend()
	plt.show()
	
	return linear_mod.predict(x)[0][0], linear_mod.coef_[0][0], linear_mod.intercept_[0]

get_data('goog.csv') # calling get_data method by passing the csv file to it
print "Dates- ", dates
print "Prices- ", prices

predicted_price, coefficient, constant = predict_price(dates, prices, 29)  
print "\nThe stock open price for 29th Feb is: $", str(predicted_price)
print "The regression coefficient is ", str(coefficient), ", and the constant is ", str(constant)
print "the relationship equation between dates and prices is: price = ", str(coefficient), "* date + ", str(constant)
