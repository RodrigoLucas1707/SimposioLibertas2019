from django.shortcuts import render
from .Aluno import Aluno
from .Submissao import Submissao
from .Autores import Autores
from .Area import Area
from .Professor import Professor
from .Avaliacao import Avaliacao
from rest_framework import generics
from .serializers import AlunoSerializer
from .serializers import AlunosSerializer
from .serializers import SubmissaoSerializer
from .serializers import AutoresSerializer
from .serializers import AvaliacaoSerializer
from .serializers import AreaSerializer
from .serializers import ProfessorSerializer

#class AlunoList(generics.ListCreateAPIView):
#    usuario = self.request.usuario
#    queryset = Aluno.objects.all()
#    serializer_class = AlunoSerializer
#class AlunoList(generics.ListAPIView):
#    serializer_class = AlunoSerializer
#    def get_queryset(self):
#        usuario = self.request.usuario
#        return Aluno.objects.filter(usuario=usuario)
class AlunosList(generics.ListAPIView):
    serializer_class = AlunosSerializer
    model = serializer_class.Meta.model
    paginate_by = 100
    def get_queryset(self):
        usuario = self.kwargs['usuario']
        queryset = self.model.objects.filter(usuario=usuario)
        return queryset

class LoginList(generics.ListAPIView):
    serializer_class = AlunoSerializer
    model = serializer_class.Meta.model
    paginate_by = 100
    def get_queryset(self):
        usuario = self.kwargs['usuario']
        senha = self.kwargs['senha']
        queryset = self.model.objects.filter(usuario=usuario, senha=senha)
        return queryset

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

class AlunoList(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer   

# Create your views here.

def simposio(request):
    return render(request, 'simposio.page/simposio.html',{})    

def css(request): 
    return render(request, 'styles.css', {},  content_type="text/css")   

def script(request):
    return render(request, 'script.js',{}, content_type="text/js")

def login(request):
    return render(request, 'paginalogin.page/Pagina-login.html',{})

def cadastro(request):
    return render(request, 'paginacadastro.page/cadastro.html', {})

def novaSub(request):
    return render(request, 'novaSubmissao.page/novasubmissao.html', {})
