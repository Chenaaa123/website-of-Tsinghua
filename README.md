## 项目说明（hengDaProject）

本项目是一个基于 Django 2.2.4 的门户网站/实验教学项目，包含“首页、公司简介（或学校简介）、新闻动态、产品中心、服务支持、科研基地、人才招聘”等模块。项目内置后台管理（SimpleUI 美化）、富文本编辑（DjangoUeditor）、全文检索（Haystack + Whoosh）、资料下载、简历投递与邮件通知、OpenCV 人脸检测等功能。

### 亮点概览
- 首页卡片式展示新闻展报/通知公告/热门产品，页面缓存15分钟
- 新闻模块支持富文本、图片、浏览量、分页与检索
- 产品模块支持按类别筛选、浏览量统计与详情
- 服务支持包含下载中心（流式下载）与人脸检测 API/Demo
- 招聘模块支持表单上传、状态流转自动邮件通知与 docx 模板生成
- 全站中文与中国时区、SimpleUI 管理后台

---

## 技术栈与依赖

- 后端框架: Django 2.2.4
- 管理后台: `simpleui`
- 富文本: `DjangoUeditor`
- 搜索: `django-haystack` + Whoosh
- 表单增强: `django-widget-tweaks`
- 页面缓存/后端缓存: `cache_page` + DatabaseCache
- 邮件: SMTP(TLS)（QQ 邮箱）
- 文档生成: `docxtpl`, `python-docx`
- 计算机视觉: `opencv-python`, `numpy`
- HTML 解析: `pyquery`
- 其他: `requests`

建议的 `requirements.txt`（版本可按教学环境灵活调整）:
```txt
Django==2.2.4
django-simpleui
django-haystack
Whoosh
DjangoUeditor
django-widget-tweaks
docxtpl
python-docx
pyquery
opencv-python
numpy
requests
```

---

## 目录结构

```text
hengDaProject10086/
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

## 全局配置要点（`hengDaProject/settings.py`）

- INSTALLED_APPS:
  - `homeApp`, `aboutApp`, `contactApp`, `newsApp`, `productsApp`, `serviceApp`, `scienceApp`
  - 第三方：`DjangoUeditor`, `haystack`, `widget_tweaks`, `simpleui`
- 国际化：`LANGUAGE_CODE='zh-Hans'`，`TIME_ZONE='Asia/Shanghai'`
- 静态/媒体：
  - `STATICFILES_DIRS = [BASE_DIR / 'static']`
  - `MEDIA_URL = '/media/'`，`MEDIA_ROOT = BASE_DIR / 'media/'`
- 搜索（Haystack + Whoosh）：
  - ENGINE=`newsApp.whoosh_backend.WhooshEngine`
  - PATH=`BASE_DIR / 'whoosh_index'`
  - 每页10条，RealtimeSignalProcessor
- 缓存：
  - DatabaseCache，表名 `cache_table_home`，超时 600s，最大并发 2000
- 邮件（QQ 邮箱示例）：
  - `EMAIL_HOST='smtp.qq.com'`, `EMAIL_PORT=25`, `EMAIL_USE_TLS=True`
- SimpleUI：
  - 默认主题 `admin.lte.css`，关闭广告与分析
- 开发设置：
  - `DEBUG=True`，`ALLOWED_HOSTS=['*']`

---

## 路由设计（`hengDaProject/urls.py` 与各 App `urls.py`）

- 根路由：
  - `/` → `homeApp.views.home`
  - `/admin/` → Django Admin（SimpleUI）
  - `/aboutApp/`、`/contactApp/`、`/newsApp/`、`/productsApp/`、`/scienceApp/`、`/serviceApp/`
  - `/ueditor/` → `DjangoUeditor`
  - `/search/` → Haystack 路由
  - `DEBUG=True` 时 `/media/` 静态托管
- 典型 App 路由：
  - `aboutApp`: `/aboutApp/survey/`、`/aboutApp/honor/`
  - `newsApp`:
    - 列表：`/newsApp/news/<company|industry|...>/`
    - 详情：`/newsApp/newDetail/<id>/`
    - 搜索：`/newsApp/search/`
  - `productsApp`:
    - 列表：`/productsApp/products/<robot|monitor|...>/`
    - 详情：`/productsApp/productDetail/<id>/`
  - `serviceApp`:
    - 下载：`/serviceApp/download/`，单项下载：`/serviceApp/getDoc/<id>/`
    - 平台：`/serviceApp/platform/`
    - API：`/serviceApp/facedetect/`（POST）
    - Demo：`/serviceApp/facedetectDemo/`（POST）
  - `contactApp`:
    - 联系：`/contactApp/contact/`
    - 招聘：`/contactApp/recruit/`

---

## 数据模型

- `aboutApp.Award`
  - `description(TextField)`、`photo(ImageField)`
  - verbose：学校荣誉
- `newsApp.MyNew`
  - `title`、`description(UEditorField)`、`newType(choices)`、`publishDate`、`views`、`photo`
  - 排序：`-publishDate`
- `productsApp.Product` / `ProductImg`
  - `Product`: `title/description/productType/price/publishDate/views`
  - `ProductImg`: `product(FK, related_name='productImgs')`、`photo`
- `serviceApp.Doc`
  - `title/file/publishDate`（文件位于 `media/Service/`）
- `contactApp.Ad`（招聘广告）
  - `title/description/publishDate`
- `contactApp.Resume`（简历）
  - 基本信息/照片/经历/状态（1未审/2通过/3未通过）/提交时间
  - 信号（`post_init`、`post_save`）:
    - 状态 1→2：邮件通知 + 基于 `media/contact/recruit.docx` 模板生成个性化 DOCX（含头像）
    - 状态 1→3：发送未通过邮件
- `scienceApp`：当前无模型

---

## 视图与业务逻辑

### 首页 `homeApp.views.home`
- `@cache_page(60*15)` 页面缓存 15 分钟
- 新闻展报：取有 `photo` 的最新 3 条
- 新闻列表：最新 7 条
- 通知公告：`newType='最新动态'` 取前 4 条
- 产品中心：按 `views` 排名前 4 条

### 新闻 `newsApp.views`
- 列表 `news(newName)`：
  - URL 参数映射：`company→综合时讯`，`industry→交流合作`，其他→`最新动态`
  - `pyquery` 从富文本中抽取 `<p>` 文本作为摘要
  - `Paginator` 分页（5条/页），自定义页码导航上下文（首末省略）
- 详情 `newDetail(id)`：
  - `views += 1` 后保存
- 搜索 `search`：
  - 简单标题包含检索（另有 `/search/` 使用 Haystack）

### 产品 `productsApp.views`
- 列表 `products(productName)`：
  - `robot→艺术博物馆`，`monitor→科学博物馆`，其他→`新清华学堂`
  - `Paginator` 分页（2条/页），同样的页码导航逻辑
- 详情 `productDetail(id)`：
  - `views += 1` 后保存

### 服务支持 `serviceApp.views`
- 下载 `download`：
  - `Doc` 列表（5 条/页）
- 单项下载 `getDoc(id)`：
  - 通过 `StreamingHttpResponse` 按 512 字节分块流式下载
- 平台 `platform`：
  - 渲染 `platForm.html`
- 人脸检测 API `facedetect`（POST）：
  - 接收 `image` 文件 → 灰度化 → `CascadeClassifier` 检测 → 返回 JSON：
    - `#faceNum` 人脸数量
    - `faces` 检测框坐标数组（左上/右下）
- 人脸检测 Demo `facedetectDemo`（POST）：
  - 在原图上绘制检测框 → 返回标注图片的 `base64` 编码字符串

注意：分类器文件路径默认 `serviceApp/haarcascade_frontalface_default.xml`，需保证部署环境可访问。

### 招聘 `contactApp.views`
- `contact`：联系我们页面
- `recruit`：展示招聘信息 + 简历表单（`ResumeForm`）
  - `POST` 合法即保存 → `success.html`
- `Resume` 状态流转触发信号：
  - 通过：邮件 + 生成个性化 `docx`
  - 未通过：邮件通知

---

## 模板与前端

- 基础模板：`templates/base.html`（各页面通过 `active_menu/sub_menu` 控制导航高亮）
- App 模板：
  - `home.html`、`survey.html`、`honor.html`
  - `newList.html`、`newDetail.html`、`searchList.html`
  - `productList.html`、`productDetail.html`
  - `docList.html`、`platForm.html`
  - `contact.html`、`recruit.html`、`success.html`
- 静态资源：`static/`（Bootstrap 样式、JS、图标、图片等）
- 媒体资源：`media/`（新闻图片、产品图片、简历照片、资料文件、模板 `contact/recruit.docx`）

---

## 搜索功能（Haystack + Whoosh）

- 配置在 `settings.py`，索引目录 `whoosh_index/`
- 每页 10 条，`RealtimeSignalProcessor` 支持数据保存时实时更新索引
- 索引模板：`templates/search/indexes/newsApp/MyNew_text.txt`
- 路由：`/search/`（Haystack），`/newsApp/search/`（标题包含检索）

---

## 缓存策略

- 页面缓存：`homeApp.views.home` 使用 `@cache_page(60*15)`
- 后端缓存：DatabaseCache，表 `cache_table_home`（首次需创建）

初始化命令：
```bash
python manage.py createcachetable cache_table_home
```

---

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

#   w e b s i t e - o f - T s i n g h u a  
 #   w e b s i t e - o f - T s i n g h u a  
 #   w e b s i t e - o f - T s i n g h u a  
 