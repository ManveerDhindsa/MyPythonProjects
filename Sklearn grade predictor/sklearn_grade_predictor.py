from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from sklearn import metrics

data = pd.read_csv('student-mat.csv', sep=";")

X = data[['G1', 'G2', 'Medu', 'Fedu', 'traveltime', 'studytime', 'failures', 'freetime']]

y = data[['G3']]

# print(X.shape)
# print(y.shape)

# print(X)
# print('_____________________________________________________________')
# print(y)

lin_reg = linear_model.LinearRegression()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15)

# print(X_test.shape)
# print(y_test.shape)

model = lin_reg.fit(X_train, y_train)

predictions = model.predict(X_test)


# print(predictions.shape)

# for z in range(len(predictions)):
#     print('Predictions:', predictions[z], end="")
#     print('Actual:', y_test[z])
    
acc = lin_reg.score(X_test, y_test)
print('Accuracy:', acc)