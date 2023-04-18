from django import forms
from predict_risk_1.models import Predictions_1

class Predict_Form_1(forms.ModelForm):
    class Meta:
        model = Predictions_1
        fields = ('age','bp','sg','al','su','rbc','pc','pcc',
        'ba','bgr','bu','sc','sod','pot','hemo','pcv','wc','rc','htn','dm','cad','appet','pe','ane')
        widgets = {
                   'age': forms.TextInput(attrs={'class': 'form-control'}),
                   'bp':forms.TextInput(attrs={'class': 'form-control'}),
               'sg':forms.Select(attrs={'class': 'form-control'}),
               'al':forms.Select(attrs={'class': 'form-control'}),
               'su':forms.Select(attrs={'class': 'form-control'}),
               'rbc':forms.Select(attrs={'class': 'form-control'}),
               'pc':forms.Select(attrs={'class': 'form-control'}),
               'pcc':forms.Select(attrs={'class': 'form-control'}),
               'ba':forms.Select(attrs={'class': 'form-control'}),
               'bgr':forms.TextInput(attrs={'class': 'form-control'}),
               'bu':forms.TextInput(attrs={'class': 'form-control'}),
               'sc':forms.TextInput(attrs={'class': 'form-control'}),
               'sod':forms.TextInput(attrs={'class': 'form-control'}),
               'pot':forms.TextInput(attrs={'class': 'form-control'}),
                'hemo':forms.TextInput(attrs={'class': 'form-control'}),
                'pcv':forms.TextInput(attrs={'class': 'form-control'}),
                'wc':forms.TextInput(attrs={'class': 'form-control'}),
                 'rc':forms.TextInput(attrs={'class': 'form-control'}),
                'htn':forms.Select(attrs={'class': 'form-control'}),
                'dm':forms.Select(attrs={'class': 'form-control'}),
                'cad':forms.Select(attrs={'class': 'form-control'}),
               'appet':forms.Select(attrs={'class': 'form-control'}),
               'pe':forms.Select(attrs={'class': 'form-control'}),
               'ane':forms.Select(attrs={'class': 'form-control'}),
              }
