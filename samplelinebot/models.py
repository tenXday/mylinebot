from django.db import models

# Create your models here.

class Script_type(models.Model):
    type = models.CharField(max_length=100, help_text="請輸入劇本類型")  
    photo = models.URLField(max_length=500, help_text="請輸入類型示意圖")
class Script_pnumber(models.Model):
    pnumber = models.CharField(max_length=100, help_text="請輸入劇本人數")  
    photo = models.URLField(max_length=500, help_text="請輸入類型示意圖")      
class Script_list(models.Model):
    sname = models.CharField(max_length=100, help_text="請輸入劇本名稱")
    photo = models.URLField(max_length=500, help_text="請輸入劇本示意圖")
    type=models.CharField(max_length=100, help_text="請輸入劇本題材")
    pnumber=models.CharField(max_length=100, help_text="請輸入人數")
    intro=models.CharField(max_length=500, help_text="請輸入介紹")

