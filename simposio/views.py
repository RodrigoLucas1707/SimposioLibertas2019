from django.shortcuts import render
from .Aluno import Aluno
from .Submissao import Submissao
from .Autores import Autores
from .Area import Area
from .Professor import Professor
from .Avaliacao import Avaliacao
from rest_framework import generics
from .serializers import AlunoSerializer
from .serializers import SubmissaoSerializer
from .serializers import AutoresSerializer
from .serializers import AvaliacaoSerializer
from .serializers import AreaSerializer
from .serializers import ProfessorSerializer

class AlunoList(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class SubmissaoList(generics.ListCreateAPIView):
    queryset = Submissao.objects.all()
    serializer_class = SubmissaoSerializer

class AutoresList(generics.ListCreateAPIView):
    queryset = Autores.objects.all()
    serializer_class = AutoresSerializer    

class AvaliacaoList(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

class AreaList(generics.ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class ProfessorList(generics.ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer            

# Create your views here.

def simposio(request):
    return render(request, 'simposio.page/simposio.html',{})    

def css(request): 
    return render(request, 'simposio.page/styles.css', {})   

