# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random


# Importing the dataset
#DIR='C:/Users/Mansi/Desktop/Heart_disease_prediction_project/predict_risk/machine_learning_models'

# Importing the dataset
dataset = pd.read_csv('kidney_disease2.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,24].values


#handling missing data

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:,:24])
X[:,:24] = imputer.transform(X[:,:24])


#splitting dataset into training set and test set

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.50,random_state=101)

#feature scaling

from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
from sklearn.externals import joblib
# Save it
scaler_file = "standard_scalar_logistic.pkl"
joblib.dump(sc_X, scaler_file)

X_test=sc_X.transform(X_test)

#exploring the dataset

# import matplotlib.pyplot as plt
# def draw_histograms(dataframe, features, rows, cols):
#     fig=plt.figure(figsize=(20,20))
#     for i, feature in enumerate(features):
#         ax=fig.add_subplot(rows,cols,i+1)
#         dataframe[feature].hist(bins=20,ax=ax,facecolor='midnightblue')
#         ax.set_title(feature+" Distribution",color='DarkRed')
#
#     fig.tight_layout()
#     plt.show()
# draw_histograms(dataset,dataset.columns,6,3)
#
#
# dataset.num.value_counts()
# import seaborn as sn
# sn.countplot(x='classification',data=dataset)
#
#
# #VISULAIZATIONS----relationship between attributes
#
# pd.crosstab(dataset.thal,dataset.num).plot(kind='bar')
# plt.title('bar chart for ane vs classification')
# plt.xlabel('ane')
# plt.ylabel('classification')
#
# pd.crosstab(dataset.trestbps,dataset.num).plot(kind='bar')
# plt.title('bar chart for pe vs classification')
# plt.xlabel('pe')
# plt.ylabel('classification')
#
# pd.crosstab(dataset.cp,dataset.num).plot(kind='bar')
# plt.title('bar chart for ca vs classification')
# plt.xlabel('ca')
# plt.ylabel('classification')
#
# pd.crosstab(dataset.chol,dataset.num).plot(kind='bar')
# plt.title('bar chart for slope vs classification')
# plt.xlabel('slope')
# plt.ylabel('classification')
#
# pd.crosstab(dataset.restecg,dataset.num).plot(kind='bar')
# plt.title('bar chart for oldpeak vs classification')
# plt.xlabel('oldpeak')
# plt.ylabel('classification')


####------------similarly can be seen for all the attributes------------------

#### logistic regression

#fitting LR to training set

from sklearn.linear_model import LogisticRegression
classifier =LogisticRegression()
classifier.fit(X_train,Y_train)


#Saving the model to disk
from sklearn.externals import joblib
filename = 'Logistic_regression_model.pkl'
joblib.dump(classifier,filename)


#Predict the test set results

y_Class_pred=classifier.predict(X_test)

#checking the accuracy for predicted results

from sklearn.metrics import accuracy_score
accuracy_score(Y_test,y_Class_pred)

# Making the Confusion Matrix

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, y_Class_pred)

#Interpretation:

from sklearn.metrics import classification_report
print(classification_report(Y_test, y_Class_pred))


#ROC
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
logit_roc_auc = roc_auc_score(Y_test, classifier.predict(X_test))
fpr, tpr, thresholds = roc_curve(Y_test, classifier.predict_proba(X_test)[:,1])
plt.figure()
plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.savefig('Log_ROC')
plt.show()

##PREDICTION FOR NEW DATASET

Newdataset = pd.read_csv('newdata.csv')
ynew=classifier.predict(Newdataset)
