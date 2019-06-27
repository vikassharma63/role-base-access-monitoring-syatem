from django.db import models
from datetime import datetime

class Logs(models.Model):
    u_name=models.CharField(max_length=25)
    passwd=models.CharField(max_length=25)
    role=models.CharField(max_length=5)
    repasswd = models.CharField(max_length=25)

class System(models.Model):
    s_name=models.CharField(max_length=25)
    s_type=models.CharField(max_length=30)
    s_work=models.CharField(max_length=250)

class Module(models.Model):
    System=models.ForeignKey(System,on_delete=models.CASCADE)
    m_name = models.CharField(max_length=25)
    m_type = models.CharField(max_length=30)
    m_work = models.CharField(max_length=250)
class Daily(models.Model):
    s_name=models.CharField(max_length=25)
    m_name = models.CharField(max_length=25)
    status = models.CharField(max_length=5)
    remark = models.CharField(max_length=250)



def __str__(self):
    return self.name
