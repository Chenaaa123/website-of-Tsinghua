from django.db import models


# Create your models here.
class Award(models.Model):  # 荣誉模型
    description = models.TextField(max_length=500,
                                   blank=True,
                                   null=True,
                                   verbose_name='领导介绍')
    photo = models.ImageField(upload_to='Award/',
                              blank=True,
                              verbose_name='历任领导')

    class Meta:
        verbose_name = '学校荣誉'          #模型定义的别名
        verbose_name_plural = '学校荣誉'   #别名对应的复数形式
