# -*- coding: utf-8 -*-
"""Breast Cancer

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18RKainaNYalaTDECDnGMkXKGv1WK3Wph

# **Data Pre Processing**

**Import**
"""

import numpy as np
import pandas as pd
import xgboost
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

#Reading
dataset = sklearn.datasets.load_breast_cancer()

#Making Dataframe
dataset_df = pd.DataFrame(dataset.data, columns=dataset.feature_names)

# Adding target as 'Label' Column
dataset_df['Label'] = dataset.target

dataset_df.head()

"""**Splitting**"""

X = dataset_df.drop(columns='Label', axis=1)
Y = dataset_df['Label']

print(Y)

"""# **Training**"""

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=2)

model = xgboost.XGBClassifier()

model.fit(X_train, Y_train)

"""# **Evaluation**

**Accuracy of Train Data**
"""

Xtrain_prediction = model.predict(X_train)
accuracy = accuracy_score(Y_train, Xtrain_prediction)

print("Accuracy of Train Data:", accuracy)

"""# **Accuracy of Test Data**"""

Xtest_prediction = model.predict(X_test)
accuracy = accuracy_score(Y_test, Xtest_prediction)

print("Accuracy of Test Data:", accuracy)