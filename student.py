import pandas as pd

data = pd.read_csv("C:\\Users\\PC\\Downloads\\linreg_dataset\\random2.csv", header=None, delimiter=',')
df = pd.DataFrame(data)
weight_0 = 0
weight_1 = 0
weight_2 = 0
iteration_number = 0
learningRate = 0.0001
threshold = 0.0001
diff = 1
squared_sum_of_errors = 0
while diff > threshold:
    gradient_0 = 0
    gradient_1 = 0
    gradient_2 = 0
    squared_sum_of_errors_current = 0
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
