from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.simposio, name='simposio'),
    path('styles.css', views.css, name='css'),
    path('login',views.login, name='login'),
    path('csslogin', views.css, name='csslogin'),
    url(r'^alunos/$', views.AlunoList.as_view(), name='aluno-list'),
    url(r'^submissao/$', views.SubmissaoList.as_view(), name='submissao-list'),
    url(r'^autores/$', views.AutoresList.as_view(), name='autores-list'),
    url(r'^area/$', views.AreaList.as_view(), name='area-list'),
    url(r'^avaliacao/$', views.AvaliacaoList.as_view(), name='avaliacao-list'),
    url(r'^professor/$', views.ProfessorList.as_view(), name='professor-list'),
]