#!/usr/bin/env python3
# coding: utf-8

import pandas as pd
import argparse

# create parser
parser = argparse.ArgumentParser()

def linear_regression():
    # accept parameters from the command line
    parser.add_argument("--data")
    parser.add_argument("--eta")
    parser.add_argument("--threshold")

    args = parser.parse_args()

    df = pd.read_csv(args.data)
    weight_0 = 0
    weight_1 = 0
    weight_2 = 0
    iteration_number = 0
    learningRate = float(args.eta)
    threshold = float(args.threshold)
    diff = 1
    squared_sum_of_errors = 0
    while diff > threshold:

        # if we decide to make the script more flexible, we can proceed as follows (this piece of code is for gradient, but we can adapt it for weights and Xs):
        """
        # retrieve the number of columns
        grad = list(range(len(df.columns)))

        # create a dictionary of variables gradient_
        c = {str("gradient_" + str(i)): 0 for i in grad}

        # create as many gradient values as columns: gradient_0 = 0, gradient_1 = 0, gradient_2 = 0
        for k, v in c.items():
            exec("%s=%s" % (k, v))
        """

        squared_sum_of_errors_current = 0
        gradient_0 = 0
        gradient_1 = 0
        gradient_2 = 0

        for i in range(len(df)):
            x_0 = 1
            x_1 = df.iat[i, 0]
            x_2 = df.iat[i, 1]
            y = df.iat[i, 2]
            y_current = weight_0 * x_0 + weight_1 * x_1 + weight_2 * x_2
            gradient_0 = gradient_0 + x_0 * (y - y_current)
            gradient_1 = gradient_1 + x_1 * (y - y_current)
            gradient_2 = gradient_2 + x_2 * (y - y_current)
            squared_sum_of_errors_current = squared_sum_of_errors_current + ((y - y_current) ** 2)
        print(iteration_number, round(weight_0, 4), round(weight_1, 4), round(weight_2, 4),
              round(squared_sum_of_errors_current, 4))
        diff = abs(squared_sum_of_errors - squared_sum_of_errors_current)
        squared_sum_of_errors = squared_sum_of_errors_current
        weight_0 = weight_0 + learningRate * gradient_0
        weight_1 = weight_1 + learningRate * gradient_1
        weight_2 = weight_2 + learningRate * gradient_2

        iteration_number = iteration_number + 1

linear_regression()
