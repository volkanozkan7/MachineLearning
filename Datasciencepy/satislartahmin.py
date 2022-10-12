# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 13:35:25 2022

@author: Volkan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veriler = pd.read_csv("satislar.csv")
print(veriler)

aylar = veriler[["Aylar"]]
print(aylar)

satislar = veriler[["Satislar"]]
print(satislar)

satislar2 = veriler.iloc[:,:1].values
print(satislar2)

from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(aylar,satislar,test_size= 0.33,random_state = 0)

from sklearn.preprocessing import StandardScaler 
sc = StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)
Y_train = sc.fit_transform(y_train)
Y_test = sc.fit_transform(y_test)

#Model inşası linear regression
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train,y_train)

tahmin = lr.predict(x_test)
x_train = x_train.sort_index()      #verilerde aylar karışık sıralanmıştı bunları düzgün sıralıcak
y_train = y_train.sort_index() 

plt.plot(x_train,y_train)
plt.plot(x_test,lr.predict(x_test))

plt.title("Aylara Göre Satış")
plt.xlabel("Aylar")
plt.ylabel("Satışlar")
