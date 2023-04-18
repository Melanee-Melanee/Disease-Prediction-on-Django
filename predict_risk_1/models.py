from django.db import models
from accounts.models import UserProfileInfo
from django.utils import timezone
from django.re_paths import reverse
# Create your models here.
sg_choices=((1.01,'1.01'),(1.02,'1.02'),(1.015,'1.015'),(1.025,'1.025'))
al_choices=((0,'0.0'),(1,'1.0'),(2,'2.0'),(3,'3.0'),(4,'4.0'))
su_choices=((0,'0.0'),(1,'1.0'),(2,'2.0'),(3,'3.0'),(4,'4.0'))
rbc_choices=((1,'normal'),(0,'abnormal'))
pc_choices=((1,'normal'),(0,'abnormal'))
pcc_choices=((1,'present'),(0,'notpresent'))
ba_choices=((1,'present'),(0,'notpresent'))
htn_choices=((1,'Yes'),(0,'No'))
dm_choices=((1,'Yes'),(0,'No'))
cad_choices=((1,'Yes'),(0,'No'))
appet_choices=((1,'good'),(0,'poor'))
pe_choices=((1,'Yes'),(0,'No'))
ane_choices=((1,'Yes'),(0,'No'))
classification_choices=((1,'ckd'),(0,'nockd'))




class Predictions_1(models.Model):
    profile = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE, related_name='predict_1')
    age = models.IntegerField(default=33)
    bp=models.IntegerField(default=80)
    sg=models.FloatField(choices=sg_choices,default=1.01)
    al=models.IntegerField(choices=al_choices,default=0)
    su=models.IntegerField(choices=su_choices,default=0)
    rbc=models.IntegerField(choices=rbc_choices,default=1)
    pc=models.IntegerField(choices=pc_choices,default=1)
    pcc=models.IntegerField(choices=pcc_choices,default=0)
    ba=models.IntegerField(choices=ba_choices,default=0)
    bgr=models.FloatField(default=89)
    bu=models.IntegerField(default=19)
    sc=models.FloatField(default=1)
    sod=models.FloatField(default=144)
    pot=models.FloatField(default=5)
    hemo=models.FloatField(default=15)
    pcv=models.IntegerField(default=40)
    wc=models.IntegerField(default=10300)
    rc=models.FloatField(default=5)
    htn=models.IntegerField(choices=htn_choices,default=0)
    dm=models.IntegerField(choices=dm_choices,default=0)
    cad=models.IntegerField(choices=cad_choices,default=0)
    appet=models.IntegerField(choices=appet_choices,default=1)
    pe=models.IntegerField(choices=pe_choices,default=0)
    ane=models.IntegerField(choices=ane_choices,default=0)



    predicted_on = models.DateTimeField(default=timezone.now)
    classification=models.IntegerField(choices=classification_choices,default=1)

    def get_absolute_re_path(self):
        return reverse('predict_1:predict_1', kwargs={'pk': self.profile.pk})
