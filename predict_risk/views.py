import csv,io
from django.shortcuts import render
from .forms import Predict_Form
from predict_risk.data_provider import *
from accounts.models import UserProfileInfo
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required,permission_required
from django.re_paths import reverse
from django.contrib import messages

@login_required(login_re_path='/')
def PredictRisk(request,pk):
    predicted = False
    predictions={}
    if request.session.has_key('user_id'):
        u_id = request.session['user_id']

    if request.method == 'POST':
        form = Predict_Form(data=request.POST)
        profile = get_object_or_404(UserProfileInfo, pk=pk)

        if form.is_valid():
            features = [[ form.cleaned_data['age'], form.cleaned_data['sex'], form.cleaned_data['cp'], form.cleaned_data['resting_bp'], form.cleaned_data['serum_cholesterol'],
            form.cleaned_data['fasting_blood_sugar'], form.cleaned_data['resting_ecg'], form.cleaned_data['max_heart_rate'], form.cleaned_data['exercise_induced_angina'],
            form.cleaned_data['st_depression'], form.cleaned_data['st_slope'], form.cleaned_data['number_of_vessels'], form.cleaned_data['thallium_scan_results']]]

            print("Before------",features)
            standard_scalar = GetStandardScalarForHeart()
            features = standard_scalar.transform(features)
            print("Hell0-------",features)
            SVCClassifier,LogisticRegressionClassifier,NaiveBayesClassifier,DecisionTreeClassifier,NeuralNetworkClassifier,KNNClassifier=GetAllClassifiersForHeart()


            predictions = {'SVC': str(SVCClassifier.predict(features)[0]),
            'LogisticRegression': str(LogisticRegressionClassifier.predict(features)[0]),
             'NaiveBayes': str(NaiveBayesClassifier.predict(features)[0]),
             'DecisionTree': str(DecisionTreeClassifier.predict(features)[0]),
              'NeuralNetwork': str(NeuralNetworkClassifier.predict(features)[0]),
              'KNN': str(KNNClassifier.predict(features)[0]),
              }
            pred = form.save(commit=False)

            l=[predictions['SVC'],predictions['LogisticRegression'],predictions['NaiveBayes'],predictions['DecisionTree'],predictions['NeuralNetwork'],predictions['KNN']]
            count=l.count('1')

            result=False

            if count>=3:
                result=True
                pred.num=1
            else:
                pred.num=0

            pred.profile = profile

            pred.save()
            predicted = True

            colors={}

            if predictions['SVC']=='0':
                colors['SVC']="table-success"
            elif predictions['SVC']=='1':
                colors['SVC']="table-danger"

            if predictions['LogisticRegression']=='0':
                colors['LR']="table-success"
            else:
                colors['LR']="table-danger"

            if predictions['NaiveBayes']=='0':
                colors['NB']="table-success"
            else:
                colors['NB']="table-danger"

            if predictions['DecisionTree']=='0':
                colors['DT']="table-success"
            else:
                colors['DT']="table-danger"

            if predictions['NeuralNetwork']=='0':
                colors['NN']="table-success"
            else:
                colors['NN']="table-danger"

            if predictions['KNN']=='0':
                colors['KNN']="table-success"
            else:
                colors['KNN']="table-danger"

    if predicted:
        return render(request, 'predict.html',
                      {'form': form,'predicted': predicted,'user_id':u_id,'predictions':predictions,'result':result,'colors':colors})

    else:
        form = Predict_Form()

        return render(request, 'predict.html',
                      {'form': form,'predicted': predicted,'user_id':u_id,'predictions':predictions})
