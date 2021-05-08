#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
from pandas.plotting import scatter_matrix
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.utils import shuffle
from sklearn.preprocessing import LabelEncoder


dataframe=pd.read_csv('movies_data/data3.csv')
# dataframe = dataframe.sample(frac = 1)








class GetRating():
    def __init__(self,minutes,shops,rating):
        self.minutes=minutes
        self.shops=shops
        self.rating=rating
#         print(self.minutes)
#         print(self.shops)
#         print(self.rating)

    def getrating(self):
#         dataframe=pd.read_csv('movies_data/data2.csv')
#         dataframe = dataframe.sample(frac = 1)
        array=dataframe.values
        
        X=array[:,[3,4,5]]
        Y=array[:,[7]]
        Y=Y.astype('int')
    
        

        X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=0.2, random_state=0)


        model= RandomForestClassifier()
        model.fit(X_train,Y_train)

        y_pred=model.predict(X_validation)

        print('Acurracy of training set ',(model.score(X_train, Y_train)*100))
        print('Acurracy of testing set ',(accuracy_score(Y_validation, y_pred)*100))
        print ("Accuracy : ", accuracy_score(Y_validation, y_pred)) 
        print (classification_report(Y_validation, y_pred))
        test=[self.minutes,self.shops,self.rating]
        arr = np.array(test)
        sa=model.predict(arr.reshape(1,-1)) #MODEL PREDICTED LABEL
        return dict({'Overall Rating': str(sa)})


x=GetRating(80,3,5)
val=x.getrating()
print(val)


# In[ ]:





# In[ ]:




