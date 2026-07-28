import pandas as pd
import numpy as np


class LinearRegression:
    def __init__(self, learning_rate=0.001, n_iterations=100):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weight = 0
        self.bias = 0
        self.loss = []

    @staticmethod
    def _mean_squared_error( y, y_hat):
        n = y.shape[0]
        error =  np.sum((y - y_hat) **2) / n

        return error 
    
    def _gradient_descent(self, X, y):
        de_dw = 0
        de_db = 0

        n = y.shape[0]


        y_hat = self.weight * X + self.bias

        de_dw = -(2/n) * np.dot( X , (y - y_hat))
        de_db = -(2/n) * np.sum(y - y_hat)
        
        self.weight -= self.learning_rate * de_dw
        self.bias -= self.learning_rate * de_db

    def fit(self,X,y):
        for _ in range(self.n_iterations):
            self._gradient_descent(X,y)
            y_hat = self.weight * X + self.bias
            loss = self._mean_squared_error(y, y_hat)
            self.loss.append(loss)

    def predict(self,X):
        return self.weight * X + self.bias

