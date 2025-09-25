本项目是一个基于 Django 2.2.4 仿制清华大学官网，包含“首页、公司简介（或学校简介）、新闻动态、产品中心、服务支持、科研基地、人才招聘”等模块。项目内置后台管理（SimpleUI 美化）、富文本编辑（DjangoUeditor）、全文检索（Haystack + Whoosh）、资料下载、简历投递与邮件通知、OpenCV 人脸检测等功能。

---

## 目录结构

```text
website-of-Tsinghua@README.md/
  └─ hengDaProject/
     ├─ hengDaProject/
     │  ├─ settings.py         # 全局配置
     │  └─ urls.py             # 根路由
     ├─ homeApp/               # 首页
     │  ├─ views.py
     │  └─ templates/home.html
     ├─ aboutApp/              # 公司/学校简介
     │  ├─ models.py           # Award（学校荣誉）
     │  ├─ views.py            # survey/honor
     │  ├─ urls.py
     │  └─ templates/{survey.html,honor.html}
     ├─ newsApp/               # 新闻动态
     │  ├─ models.py           # MyNew（新闻）
     │  ├─ views.py            # 列表/详情/搜索
     │  ├─ urls.py
     │  └─ templates/{newList.html,newDetail.html,searchList.html}
     ├─ productsApp/           # 产品中心
     │  ├─ models.py           # Product, ProductImg
     │  ├─ views.py            # 列表/详情
     │  ├─ urls.py
     │  └─ templates/{productList.html,productDetail.html}
     ├─ serviceApp/            # 服务支持
     │  ├─ models.py           # Doc（资料）
     │  ├─ views.py            # 下载/人脸检测API + Demo
     │  ├─ urls.py
     │  └─ templates/{docList.html,platForm.html}
     ├─ scienceApp/            # 科研基地（模板展示）
     │  └─ templates/science.html
     ├─ contactApp/            # 人才招聘
     │  ├─ models.py           # Ad, Resume + 信号
     │  ├─ views.py            # contact, recruit（表单）
     │  ├─ urls.py
     │  └─ templates/{contact.html,recruit.html,success.html}
     ├─ DjangoUeditor/         # 富文本编辑器整合
     ├─ templates/
     │  ├─ base.html           # 站点基础模板
     │  └─ search/indexes/newsApp/MyNew_text.txt  # haystack 索引模板
     ├─ static/                # 前端资源（Bootstrap/JS/图标/图片）
     ├─ media/                 # 媒体资源（图片/文档/上传）
     ├─ whoosh_index/          # Whoosh 索引目录
     ├─ db.sqlite3             # SQLite 数据库
     └─ manage.py
```

---

## 项目部分展示

### ![75880320871](C:\Users\陈大善人\AppData\Local\Temp\1758803208710.png)

![75880322085](C:\Users\陈大善人\AppData\Local\Temp\1758803220853.png)

![75880323570](C:\Users\陈大善人\AppData\Local\Temp\1758803235704.png)

![75880324349](C:\Users\陈大善人\AppData\Local\Temp\1758803243498.png)

![75880325166](C:\Users\陈大善人\AppData\Local\Temp\1758803251665.png)

![75880326589](C:\Users\陈大善人\AppData\Local\Temp\1758803265892.png)

![75880327520](C:\Users\陈大善人\AppData\Local\Temp\1758803275202.png)

![75880328573](C:\Users\陈大善人\AppData\Local\Temp\1758803285734.png)

![75880329121](C:\Users\陈大善人\AppData\Local\Temp\1758803291219.png)

![75880329699](C:\Users\陈大善人\AppData\Local\Temp\1758803296995.png)



## 运行与部署

### 本地开发
1. 安装依赖（建议虚拟环境）
2. 迁移数据库
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createcachetable cache_table_home
   ```
3. 创建管理员
   ```bash
   python manage.py createsuperuser
   ```
4. 启动服务
   ```bash
   python manage.py runserver
   ```
5. 访问：
   - 前台：`http://127.0.0.1:8000/`
   - 后台：`http://127.0.0.1:8000/admin/`


