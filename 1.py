import csv
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

age = []
salary = []

#downloaded data from https://www.google.com/finance/historical?cid=304466804484872&startdate=Jun+15%2C+2016&enddate=Jun+30%2C+2016&num=30&ei=WbVaWdHkN4fjjAG2l6OwCA
def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)  # skipping column names
        for row in csvFileReader:
            #print(', '.join(row))
            age.append(int(row[0]))
            salary.append(float(row[1]))
    return


def show_plot(age, salary):
    linear_mod = linear_model.LinearRegression()
    age = np.reshape(age, (len(age), 1))  # converting to matrix of n X 1
    salary = np.reshape(salary, (len(salary), 1))
    linear_mod.fit(age, salary)  # fitting the data points in the model
    plt.scatter(age, salary, color='yellow')  # plotting the initial datapoints
    plt.plot(age, linear_mod.predict(age), color='blue', linewidth=3)  # plotting the line made by linear regression
    plt.show()
    return


def predict_price(age, salary, x):
    linear_mod = linear_model.LinearRegression()  # defining the linear regression model
    age = np.reshape(age, (len(age), 1))  # converting to matrix of n X 1
    salary = np.reshape(salary, (len(salary), 1))
    linear_mod.fit(age, salary)  # fitting the data points in the model
    predicted_price = linear_mod.predict(x)
    return predicted_price[0][0], linear_mod.coef_[0][0], linear_mod.intercept_[0]


get_data('google.csv')  # calling get_data method by passing the csv file to it
print
age
print
salary
print
"\n"

show_plot(age, salary)
# image of the plot will be generated. Save it if you want and then Close it to continue the execution of the below code.

print("predicted values are:")
(predicted_price, coefficient, constant) = predict_price(age, salary, 1)
print("The predicted salary is: $", str(predicted_price))
print("The regression coefficient is ", str(coefficient), ", and the constant is ", str(constant))
print("the relationship equation between age and salary is: price = ", str(coefficient), "* date + ", str(constant))

