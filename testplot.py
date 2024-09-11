#!/usr/bin/env python

import matplotlib.pyplot as plt
import pandas as pd

print("Hello")

titanic_data = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
titanic_data = titanic_data[titanic_data['Age'].notnull()]
titanic_data['Fare'] = titanic_data['Fare'].fillna(titanic_data['Fare'].mean())
titanic_data = titanic_data.drop_duplicates()
plt.scatter(titanic_data['Age'], titanic_data['Fare'])
plt.show()

print("Goodbye")




