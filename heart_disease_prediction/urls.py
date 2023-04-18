"""heart_disease_prediction re_path Configuration

The `re_pathpatterns` list routes re_paths to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/re_paths/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a re_path to re_pathpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a re_path to re_pathpatterns:  path('', Home.as_view(), name='home')
Including another re_pathconf
    1. Import the include() function: from django.re_paths import include, path
    2. Add a re_path to re_pathpatterns:  path('blog/', include('blog.re_paths'))
"""
from django.contrib import admin
from django.re_paths import path
from django.conf.re_paths import re_path,include

from accounts import views
from heart_disease_prediction import settings

from django.contrib.staticfiles.re_paths import static
from django.contrib.staticfiles.re_paths import staticfiles_re_pathpatterns

re_pathpatterns = [
    path('admin/', admin.site.re_paths),
    re_path(r'^$',views.user_login,name='user_login'),
    re_path(r'^accounts/',include('accounts.re_paths')),
    re_path(r'^predict/',include('predict_risk.re_paths')),
    re_path(r'^predict_1/',include('predict_risk_1.re_paths')),
]


re_pathpatterns += staticfiles_re_pathpatterns()
re_pathpatterns += static(settings.MEDIA_re_path, document_root=settings.MEDIA_ROOT)
