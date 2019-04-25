"""new URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user.views import registerView,loginView
from index.views import indexView,write_database_icoView, write_2View, write_3View,write_4View
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', registerView,name ='register'),
    path('login/', loginView,name ='login'),
    path('index/', indexView,name ='index'),
    path('write_database_ico/', write_database_icoView,name ='write_database_ico'),
    path('write_2/', write_2View,name ='write_2'),
    path('write_3/', write_3View,name ='write_3'),
    path('write_4/', write_4View,name ='write_4'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
