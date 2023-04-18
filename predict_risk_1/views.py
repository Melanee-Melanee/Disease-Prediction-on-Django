import csv,io
from django.shortcuts import render
from .forms import Predict_Form_1
from predict_risk_1.data_provider import *
from accounts.models import UserProfileInfo
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required,permission_required
from django.re_paths import reverse
from django.contrib import messages


@login_required(login_re_path='/')
def PredictRisk_1(request,pk):
    predicted = False
    predictions={}
    if request.session.has_key('user_id'):
        u_id = request.session['user_id']

    if request.method == 'POST':
        form = Predict_Form_1(request.POST)
        print(form)
        print()
        print(request.POST)
        profile = get_object_or_404(UserProfileInfo, pk=pk)


        print("-------Enter into post-------")
        print(form.is_valid())
        if form.is_valid():

            print("----------Enter into valid---------")

            features = [[ form.cleaned_data['age'], form.cleaned_data['bp'], form.cleaned_data['sg'], form.cleaned_data['al'], form.cleaned_data['su'],
            form.cleaned_data['rbc'], form.cleaned_data['pc'], form.cleaned_data['pcc'], form.cleaned_data['ba'],
            form.cleaned_data['bgr'], form.cleaned_data['bu'], form.cleaned_data['sc'], form.cleaned_data['sod'], form.cleaned_data['pot'], form.cleaned_data['hemo'],
                          form.cleaned_data['pcv'], form.cleaned_data['wc'], form.cleaned_data['rc'], form.cleaned_data['htn'], form.cleaned_data['dm'],
                          form.cleaned_data['cad'], form.cleaned_data['appet'], form.cleaned_data['pe'], form.cleaned_data['ane']]]

            features1=features
            features2=features
            features3=features
            features4=features
            features5=features
            features6=features
            standard_scalar = GetStandardScalarForD()
            features1 = standard_scalar.transform(features1)

            standard_scalar = GetStandardScalarForL()
            features2 = standard_scalar.transform(features2)

            standard_scalar = GetStandardScalarForN()
            features3 = standard_scalar.transform(features3)

            standard_scalar = GetStandardScalarForS()
            features4 = standard_scalar.transform(features4)

            standard_scalar = GetStandardScalarForNN()
            features5 = standard_scalar.transform(features5)

            standard_scalar = GetStandardScalarForKNN()
            features6 = standard_scalar.transform(features6)


            SVCClassifier,LogisticRegressionClassifier,NaiveBayesClassifier,DecisionTreeClassifier,NNClassifier,KNNClassifier=GetAllClassifiersForKidney()

            print(features)
            predictions = {'SVC': str(SVCClassifier.predict(features1)[0]),
            'LogisticRegression': str(LogisticRegressionClassifier.predict(features2)[0]),
             'NaiveBayes': str(NaiveBayesClassifier.predict(features3)[0]),
             'DecisionTree': str(DecisionTreeClassifier.predict(features4)[0]),
              'NeuralNetwork': str(NNClassifier.predict(features5)[0]),
               'KNN': str(KNNClassifier.predict(features6)[0]),
              }
            pred = form.save(commit=False)

            print(predictions)

            l=[predictions['SVC'],predictions['LogisticRegression'],predictions['NaiveBayes'],predictions['DecisionTree'],predictions['NeuralNetwork'],predictions['KNN']]
            count=l.count('1')

            result=False

            if count>=3:
                result=True
                pred.classification=1
            else:
                pred.classification=0

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
        return render(request, 'predict_1.html',
                      {'form': form,'predicted': predicted,'user_id':u_id,'predictions':predictions,'result':result,'colors':colors})

    else:
        form = Predict_Form_1()

        return render(request, 'predict_1.html',
                      {'form': form,'predicted': predicted,'user_id':u_id,'predictions':predictions})
