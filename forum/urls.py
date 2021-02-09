from django.urls import path
from . import views, admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.forum, name='forum'),
    path('addInForum/', views.addInForum, name='addInForum'),
    path('addInDiscussion/', views.addInDiscussion, name='addInDiscussion'),
]