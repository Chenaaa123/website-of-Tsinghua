from django.db import models
from django.utils import timezone


# Create your models here.
class Product(models.Model):
    PRODUCTS_CHOICES = (
        ('艺术博物馆', '艺术博物馆'),
        ('科学博物馆', '科学博物馆'),
        ('新清华学堂', '新清华学堂'),          #一个下拉选择框
    )
    title = models.CharField(max_length=50, verbose_name='展品标题')
    description = models.TextField(verbose_name='展品描述')
    productType = models.CharField(choices=PRODUCTS_CHOICES,
                                   max_length=50,
                                   verbose_name='建筑类型')
    price = models.DecimalField(max_digits=7,
                                decimal_places=1,
                                blank=True,
                                null=True,
                                verbose_name='资金投入')
    publishDate = models.DateTimeField(max_length=20,
                                       default=timezone.now,
                                       verbose_name='发布时间')
    views = models.PositiveIntegerField('浏览量', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '学校建筑'
        verbose_name_plural = '学校建筑'
        ordering = ('-publishDate', )   #负号的作用是发布时间由近到远来显示


class ProductImg(models.Model):
    product = models.ForeignKey(Product,                        #外键 从属product类
                                related_name='productImgs',     #逆向名称
                                verbose_name='学校建筑',
                                on_delete=models.CASCADE)       #避免表里面的数据不一致
    photo = models.ImageField(upload_to='Product/',
                              blank=True,
                              verbose_name='展品图片')

    class Meta:
        verbose_name = '展品图片'
        verbose_name_plural = '展品图片'