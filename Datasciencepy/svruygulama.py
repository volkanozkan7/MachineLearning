# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 20:38:41 2022

@author: Volkan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#veri YÜKLEME
veriler = pd.read_csv("maaslar.csv")
print(veriler)

#dataframe dilimleme
x = veriler.iloc[:,1:2]
y = veriler.iloc[:,2:]

#Numpy array dönüşümü
X = x.values
Y = y.values

#Linear regression
#Doğrusal model oluşturma
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x.values,y.values)


#polynomial regression
#Doğrusal olmayan model oluşturma
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 2)
x_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,y)

                   
                #degree = 4
poly_reg3 = PolynomialFeatures(degree = 4)
x_poly3 = poly_reg3.fit_transform(X)
lin_reg3 = LinearRegression()
lin_reg3.fit(x_poly3,y)

#Görselleştirme
plt.scatter(X,Y,color="red")
plt.plot(x,lin_reg.predict(X),color = "blue")
plt.show()

plt.scatter(X,Y,color = "red")
plt.plot(X,lin_reg2.predict(poly_reg.fit_transform(X)),color = "blue")
plt.show()

plt.scatter(X,Y,color = "red")
plt.plot(X,lin_reg3.predict(poly_reg3.fit_transform(X)),color = "blue")
plt.show()

from sklearn.preprocessing import StandardScaler 
sc1 = StandardScaler()
x_scale = sc1.fit_transform(X)
sc2 = StandardScaler()
y_scale = sc2.fit_transform(Y)

from sklearn.svm import SVR
svr_reg = SVR(kernel = "rbf")
svr_reg.fit(x_scale,y_scale)

plt.scatter(x_scale,y_scale)
plt.plot(x_scale,svr_reg.predict(x_scale))

print(svr_reg.predict(11))
print(svr_reg.predict(6.6))






