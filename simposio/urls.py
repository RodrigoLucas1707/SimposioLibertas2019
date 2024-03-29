from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.login, name='login'),
    path('submissoes', views.simposio, name='simposio'),
    path('styles.css', views.css, name='css'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('novasubmissao', views.novaSub, name='novasubmissao'),
    path('script.js', views.script, name='script'),
    path('simposio.js', views.simposiojs, name='simposio'),
    url(r'^alunos/(?P<usuario>.+)/$', views.AlunosList.as_view(), name='alunos-list'),
    url(r'^login/(?P<usuario>.+)/(?P<senha>.+)/$', views.LoginList.as_view(), name='login-list'),
    url(r'^submissao/$', views.SubmissaoList.as_view(), name='submissao-list'),
    url(r'^submissaofiltro/(?P<usuario>.+)/$', views.SubmissaoFiltroList.as_view(), name='submissaofiltro-list'),
    url(r'^autores/$', views.AutoresList.as_view(), name='autores-list'),
    url(r'^area/$', views.AreaList.as_view(), name='area-list'),
    url(r'^avaliacao/$', views.AvaliacaoList.as_view(), name='avaliacao-list'),
    url(r'^professor/$', views.ProfessorList.as_view(), name='professor-list'),
    url(r'^aluno/$', views.AlunoList.as_view(), name='aluno-list'),
    url(r'^nvsubmissao/$', views.NvsubmissaoList.as_view(), name='nvsubmissao-list'),
]