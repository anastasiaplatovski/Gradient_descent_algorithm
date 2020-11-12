#!/usr/bin/env python3
# coding: utf-8

import csv
import argparse

# create parser
parser = argparse.ArgumentParser()

# accept parameters from the command line
parser.add_argument("--data")
parser.add_argument("--eta")
parser.add_argument("--threshold")

args = parser.parse_args()


def read_csv():
    with open(args.data, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    lst = []
    for i in data:
        for k in i:
            lst.append(float(k))
    data = [lst[i:i + 3] for i in range(0, len(lst), 3)]
    return data


def linear_regression():
    df = read_csv()
    weight_0 = 0
    weight_1 = 0
    weight_2 = 0
    iteration_number = 0
    learning_rate = float(args.eta)
    threshold = float(args.threshold)
    diff = 1
    squared_sum_of_errors = 0
    while diff > threshold:

        squared_sum_of_errors_current = 0
        gradient_0 = 0
        gradient_1 = 0
        gradient_2 = 0

        for i in range(len(df)):
            x_0 = 1
            x_1 = df[i][0]
            x_2 = df[i][1]
            y = df[i][2]
            y_current = weight_0 * x_0 + weight_1 * x_1 + weight_2 * x_2
            gradient_0 = gradient_0 + x_0 * (y - y_current)
            gradient_1 = gradient_1 + x_1 * (y - y_current)
            gradient_2 = gradient_2 + x_2 * (y - y_current)
            squared_sum_of_errors_current = squared_sum_of_errors_current + ((y - y_current) ** 2)
        print(str(iteration_number) + "," + str(round(weight_0, 4)) + "," + str(round(weight_1, 4)) + "," + str(
            round(weight_2, 4)) + "," +
              str(round(squared_sum_of_errors_current, 4)))
        diff = abs(squared_sum_of_errors - squared_sum_of_errors_current)
        squared_sum_of_errors = squared_sum_of_errors_current
        weight_0 = weight_0 + learning_rate * gradient_0
        weight_1 = weight_1 + learning_rate * gradient_1
        weight_2 = weight_2 + learning_rate * gradient_2

        iteration_number = iteration_number + 1


linear_regression()
