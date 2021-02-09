from django.urls import path

from . import views

app_name = 'quiz'
urlpatterns = [
    path('quiz', views.index, name='index'),
    path('quiz/<int:question_id>/', views.detail, name='detail'),
    path('quiz/<int:question_id>/results/', views.results, name='results'),
    path('quiz/<int:question_id>/respond/', views.respond, name='respond'),
]