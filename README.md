# Heart and Kidney Disease Prediction System using machine learning
>The aim of this project is to predict heart and Kidney disease using data mining techniques and machine learning algorithms.This project implements 6 classificiation models using scikit-learn: Logistic Regression, Naïve Bayes, Support Vector Classifier,KNN, Nerual Network and Decision Tree Model to investigate their performance on heart and kidney disease datasets obtained from the UCI data repository and from Kaggle.com.

All the machine learning features can be viewed here: [Machine Learning features for Heart](predict_risk/machine_learning_models) and [Machine Learning features for Kidney](predict_risk_1/machine_learning_models)

It supports following features:

*	Login/ Sign Up 
*	Viewing and Editing Profile.
*	User can enter the values of various parameters on the basis of which his risk factor will be calculated using machine learning algorithms.



<p align="center">
<img src="screenshots/Login.png" width="70%" height="70%" />
</p>

 
 <p align="center">
  <img src="screenshots/prediction_page_filled.png" width="70%" height="70%" />
 </p>
 
 
 <p align="center">
  <img src="screenshots/prediction_result.png" width="70%" height="70%" />
 </p>
                                                                           
Quick start
-----------
1. (optional) create virtual env ex. mkvirtualenv mytest_env
2. pip install -r requirements.txt
3. python manage.py migrate
4. python manage.py runserver



