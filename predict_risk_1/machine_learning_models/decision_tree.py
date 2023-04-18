# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

# Importing the dataset
dataset = pd.read_csv('kidney_disease2.csv')

X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,24].values


#handling missing data

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:,:24])
X[:,:24] = imputer.transform(X[:,:24])

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5, random_state =101)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
train=list(X_train)
X_train = sc.fit_transform(X_train)
from sklearn.externals import joblib
# Save it
scaler_file = "standard_scalar_decision.pkl"
joblib.dump(sc, scaler_file)
X_test = sc.transform(X_test)

#EXPLORING THE DATASET
import seaborn as sn
sn.countplot(x='classification',data=dataset)
dataset.classification.value_counts()
print("------",dataset.classification.value_counts(),"----------")
# Fitting Decision Tree Classification to the Training set
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)

from sklearn.externals import joblib
filename ='decision_tree_model.pkl'
joblib.dump(classifier,filename)


# Predicting the Test set results
print(X_test)
y_pred = classifier.predict(X_test)
print(y_pred)
print(y_test)

#ACCURACY SCORE
from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)

##CONFUSION MATRIX
from sklearn.metrics import classification_report, confusion_matrix
cm=confusion_matrix(y_test, y_pred)

#Interpretation:
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

#ROC
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
logit_roc_auc = roc_auc_score(y_test, classifier.predict(X_test))
fpr, tpr, thresholds = roc_curve(y_test, classifier.predict_proba(X_test)[:,1])
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
sca=StandardScaler()
train=sca.fit_transform(train)
Newdataset=sca.transform(Newdataset)
print(Newdataset)

ynew=classifier.predict(Newdataset)
print("---------",ynew,"------------")
