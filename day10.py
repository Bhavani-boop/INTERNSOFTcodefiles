# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 09:25:58 2023

@author: BHAVANI RAVI ANGADI
"""


#IMPORTING THE LIBRARIES
import matplotlib.pyplot as plt
import pandas as pd



#READING THE DATA FROM YOUR FILES
bhavani=pd.read_csv("advertising.csv")
bhavani.head()



#TO VISUALIZE DATA
fig , axs = plt.subplots(1,3,sharey=True)
bhavani.plot(kind='scatter',x='TV',y='Sales',ax=axs[0],figsize=(14,7))
bhavani.plot(kind='scatter',x='Radio',y='Sales',ax=axs[1])
bhavani.plot(kind='scatter',x='Newspaper',y='Sales',ax=axs[2])




#CREATING A&Y FOR LINEAR REGRESSION
feature_cols = ['TV']
X= bhavani[feature_cols]
y = bhavani.Sales


#IMPORTING LINEAR REGRESSION ALGO
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X,y)

print(lr.intercept_)
print(lr.coef_)




result=6.9748214882298925 + 0.05546477*50
print(result)


#CREATE  A DATAFRAME WITH MIN AND MAX VALUE OF THE TABLE
X_new = pd.DataFrame({'TV':[bhavani.TV.min(), bhavani.TV.max()]})
X_new.head()



preds = lr.predict(X_new)
preds


bhavani.plot(kind = 'scatter',x='TV',y='Sales')

plt.plot(X_new,preds,c='red',linewidth = 3)



import statsmodels.formula.api as smf
lm = smf.ols(formula = 'Sales ~ TV',data = bhavani).fit()
lm.conf_int()



#FINDING THE PROBABILITY VALUES
lm.pvalues



#FINDING THE R=SQUARED VALUES
lm.rsquared



#MULTI LINEAR REGRESSION
feature_cols = ['TV','Radio','Newspaper']
X= bhavani[feature_cols]
y = bhavani.Sales


lr = LinearRegression()
lr.fit(X,y)


print(lr.intercept_)
print(lr.coef_)



lm = smf.ols(formula='Sales ~ TV+Radio+Newspaper', data=bhavani).fit()
lm.conf_int()
lm.summary()