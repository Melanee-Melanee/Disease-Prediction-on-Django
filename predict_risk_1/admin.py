from django.contrib import admin
from predict_risk_1.models import Predictions_1
from django import forms

class Prediction_1(admin.ModelAdmin):
    list_display=('age','bp','sg','al','su','rbc','pc','pcc',
        'ba','bgr','bu','sc','sod','pot','hemo','pcv','wc','rc','htn','dm','cad','appet','pe','ane','classification')
admin.site.register(Predictions_1,Prediction_1)
