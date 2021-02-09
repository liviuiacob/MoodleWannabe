"""webApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from register import views as v
from main import views as v1
from forum import views as v2
from course import views as v3
from quiz import views as v4

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', v.register, name="register"),
    path('account/', v1.account, name="account"),
    path('changePassword/', v1.change_password, name='changePassword'),
    path('changeEmail/', v1.email_change, name='changeEmail'),
    path('', include("main.urls")),
    path('', include("django.contrib.auth.urls")),
    path('forum/', v2.forumApp, name='forum'),
    path('addInForum/', v2.addInForum, name='addInForum'),
    path('addInDiscussion/', v2.addInDiscussion, name='addInDiscussion'),
    path('course/', v3.groupApp, name='course'),
    path('addGroup/', v3.addGroup, name='addGroup'),
    path('addInUser/', v3.addInUser, name='addInUser'),
    path('uploadFile/', v3.uploadFile, name='uploadFile'),
    path('materials/', v3.studentGroup, name='studentGroup'),
    path('sendEmail/', v3.sendEmail, name='sendEmail'),
    path('', include("quiz.urls")),
    path('quiz/', v4.index, name='quiz'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
