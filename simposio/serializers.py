from rest_framework import serializers, generics
from .Aluno import Aluno
from .Submissao import Submissao
from .Autores import Autores
from .Area import Area
from .Avaliacao import Avaliacao
from .Professor import Professor




class AlunoSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField('get_likes')

    def get_likes(self, usuario):
        qs = Aluno.objects.filter(usuario=usuario)
        serializer = AlunoSerializer(instance=qs, many=True)
        print('teste: ')
        print(usuario)
        return serializer.data

    class Meta:
        model = Aluno
        fields = '__all__'



class SubmissaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Submissao
        fields = '__all__'

class AutoresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Autores
        fields = '__all__'

class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        fields = '__all__'

class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Avaliacao
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professor
        fields = '__all__'                                