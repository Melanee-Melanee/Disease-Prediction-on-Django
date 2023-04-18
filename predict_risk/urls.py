from django.conf.re_paths import re_path
from . import views
app_name='predict'
re_pathpatterns=[
re_path(r'^(?P<pk>\d+)$',views.PredictRisk,name='predict')
]
