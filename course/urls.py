from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views, admin

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.groups, name='course'),
                  path('addGroup/', views.addGroup, name='addGroup'),
                  path('addInUser/', views.addInUser, name='addInUser'),
                  path('uploadFile/', views.upload_file, name='uploadFile'),
                  path('studentGroup/', views.studentGroup, name='studentGroup'),
                  path('sendEmail/', views.sendEmail, name='sendEmail'),
              ]
