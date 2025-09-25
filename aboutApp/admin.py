
from django.contrib import admin
from .models import Award

# Register your models here.


class AwardAdmin(admin.ModelAdmin):
    list_display = ['description', 'photo']


admin.site.register(Award, AwardAdmin)

admin.site.site_header = '清华大学后台管理系统'        #管理系统头部
admin.site.site_title = '清华大学官网后台管理系统'          #页面标题


#重写admin
