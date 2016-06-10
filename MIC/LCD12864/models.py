# coding: utf-8

from django.db import models

# Create your models here.

# 字符表
class Word(models.Model):
    id = models.AutoField(primary_key = True)      #id
    vowel = models.CharField(max_length = 20)      #元音
    edittime = models.DateTimeField()              #最后一次修改时间
    state = models.SmallIntegerField()             #字符状态,0不通过,1通过
    content = models.CharField(max_length = 100)   #字符内容
    index = models.CharField(max_length = 20)      #字符引用方式
    title = models.CharField(max_length = 100)     #标题
    ttype = models.IntegerField()  				   #字符类别
    class Meta:
        db_table = 'MIC_LCD12864'