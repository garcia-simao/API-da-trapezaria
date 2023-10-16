from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario
from .serializers import UsuarioSerializer
from .models import Prato_do_dia
from .serializers import Prato_do_dia_Serializer
from .models import Funcionario
from .serializers import FuncionarioSerializer
from .models import Avaliacao_de_alimento
from .serializers import Avaliacao_de_alimentosSerializer
from .models import Avaliacao_da_cozinha
from .serializers import Avaliacao_da_cozinhaSerializer
from .models import Informacao_de_temperatura
from .serializers import Informacao_de_temperaturaSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Avaliacao_do_chefe
from .serializers import Avaliacao_do_chefeSerializer
from .models import Ocupacao
from .serializers import OcupacaoSerializer
from .models import Cozinha
from .serializers import CozinhaSerializer
from rest_framework.filters import SearchFilter, OrderingFilter


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (IsAuthenticated,)
    
    # Criacao de filtros
    def get_queryset(self):
        queryset = Usuario.objects.all()
        codigo_entrada = self.request.query_params.get('codigo_entrada')
        nome = self.request.query_params.get('nome')
        email = self.request.query_params.get('email')
        username = self.request.query_params.get('username')
        password = self.request.query_params.get('password')
        departamento = self.request.query_params.get('departamento')
        data_de_registro = self.request.query_params.get('data_de_registro')


        if codigo_entrada:
            queryset = queryset.filter(codigo_entrada=codigo_entrada)
            return queryset

        if nome:
            queryset = queryset.filter(nome=nome)
            return queryset
        
        if email:
            queryset = queryset.filter(email=email)
            return queryset

        if username:
            queryset = queryset.filter(username=username)
            return queryset

        if password:
            queryset = queryset.filter(password=password)
            return queryset

        if departamento:
            queryset = queryset.filter(departamento=departamento)
            return queryset
        
        if data_de_registro:
            queryset = queryset.filter(data_de_registro=data_de_registro)
            return queryset
        return queryset


class Prato_do_dia_ViewSet(viewsets.ModelViewSet):
    queryset = Prato_do_dia.objects.all()
    serializer_class = Prato_do_dia_Serializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('nome_do_prato','data_refeicao', 'caloria') 

    #criação de filtros
    def get_queryset(self):
        queryset = Prato_do_dia.objects.all()
        nome_do_prato = self.request.query_params.get('nome_do_prato')
        chefe = self.request.query_params.get('chefe')
        caloria = self.request.query_params.get('caloria')
        data_refeicao = self.request.query_params.get('data_refeicao')
        data_de_registro = self.request.query_params.get('data_de_registro')


        if nome_do_prato:
            queryset = queryset.filter(nome_do_prato=nome_do_prato)
            return queryset

        if chefe:
            queryset = queryset.filter(chefe=chefe)
            return queryset
        
        if caloria:
            queryset = queryset.filter(caloria=caloria)
            return queryset

        if data_refeicao:
            queryset = queryset.filter(data_refeicao=data_refeicao)
            return queryset

        if data_de_registro:
            queryset = queryset.filter(data_de_registro=data_de_registro)
            return queryset
        return queryset


#criação de filtros
class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Funcionario.objects.all()
        nome = self.request.query_params.get('nome')
        email = self.request.query_params.get('email')
        Numero_do_bilhete = self.request.query_params.get('Numero_do_bilhete')
        funcao = self.request.query_params.get('funcao')
        departamento = self.request.query_params.get('departamento')
        permissao = self.request.query_params.get('permissao')
        endereco = self.request.query_params.get('endereco')


        if nome:
            queryset = queryset.filter(nome=nome)
            return queryset

        if email:
            queryset = queryset.filter(email=email)
            return queryset
        
        if Numero_do_bilhete:
            queryset = queryset.filter(Numero_do_bilhete=Numero_do_bilhete)
            return queryset

        if funcao:
            queryset = queryset.filter(funcao=funcao)
            return queryset

        if departamento:
            queryset = queryset.filter(departamento=departamento)
            return queryset
        
        if permissao:
            queryset = queryset.filter(permissao=permissao)
            return queryset
        
        if endereco:
            queryset = queryset.filter(endereco=endereco)
            return queryset
        return queryset



class Avaliacao_de_alimentosViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao_de_alimento.objects.all()
    serializer_class = Avaliacao_de_alimentosSerializer
    permission_classes = (IsAuthenticated,)
    

    #Criação de filtros
    def get_queryset(self):
        queryset = Avaliacao_de_alimento.objects.all()
        id_do_prato = self.request.query_params.get('id_do_prato')
        numero_de_estrelas = self.request.query_params.get('numero_de_estrelas')
        id_do_usuario = self.request.query_params.get('id_do_usuario')
        data_de_registro = self.request.query_params.get('data_de_registro')

        if id_do_prato:
            queryset = queryset.filter(id_do_prato=id_do_prato)
            return queryset

        if numero_de_estrelas:
            queryset = queryset.filter(numero_de_estrelas=numero_de_estrelas)
            return queryset
        
        if id_do_usuario:
            queryset = queryset.filter(id_do_usuario=id_do_usuario)
            return queryset

        if data_de_registro:
            queryset = queryset.filter(data_de_registro=data_de_registro)
            return queryset
        return queryset

class Avaliacao_da_cozinhaViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao_da_cozinha.objects.all()
    serializer_class = Avaliacao_da_cozinhaSerializer
    permission_classes = (IsAuthenticated,)

    #Criação de filtros
    def get_queryset(self):
        queryset = Avaliacao_da_cozinha.objects.all()
        numero_de_estrelas = self.request.query_params.get('numero_de_estrelas')
        id_do_usuario = self.request.query_params.get('id_do_usuario')
        data_de_registro = self.request.query_params.get('data_de_registro')

        if id_do_usuario:
            queryset = queryset.filter(id_do_usuario=id_do_usuario)
            return queryset

        if numero_de_estrelas:
            queryset = queryset.filter(numero_de_estrelas=numero_de_estrelas)
            return queryset
        
        if data_de_registro:
            queryset = queryset.filter(data_de_registro=data_de_registro)
            return queryset
        return queryset



class Informacao_de_temperaturaViewSet(viewsets.ModelViewSet):
    queryset = Informacao_de_temperatura.objects.all()
    serializer_class = Informacao_de_temperaturaSerializer
    permission_classes = (IsAuthenticated,)

    #Criação de filtros
    def get_queryset(self):
        queryset = Informacao_de_temperatura.objects.all()
        temperatura_ambiental = self.request.query_params.get('temperatura_ambiental')
        temperatura_do_contentor = self.request.query_params.get('temperatura_do_contentor')
        data_de_registro = self.request.query_params.get('data_de_registro')

        if temperatura_ambiental:
            queryset = queryset.filter(temperatura_ambiental=temperatura_ambiental)
            return queryset
        
        if temperatura_do_contentor:
            queryset = queryset.filter(temperatura_do_contentor=temperatura_do_contentor)
            return queryset
        
        if data_de_registro:
            queryset = queryset.filter(data_de_registro=data_de_registro)
            return queryset
        return queryset

    
class Avaliacao_do_chefeViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao_do_chefe.objects.all()
    serializer_class = Avaliacao_do_chefeSerializer
    permission_classes = (IsAuthenticated,)

    #Criação de filtros
    def get_queryset(self):
        queryset = Avaliacao_do_chefe.objects.all()
        id_do_chefe = self.request.query_params.get('id_do_chefe')
        id_do_usuario = self.request.query_params.get('id_do_usuario')
        numero_de_estrelas = self.request.query_params.get('numero_de_estrelas')
        data_de_registro = self.request.query_params.get('data_de_registro')

        if id_do_chefe:
            queryset = queryset.filter(id_do_chefe=id_do_chefe)
            return queryset

        if numero_de_estrelas:
            queryset = queryset.filter(numero_de_estrelas=numero_de_estrelas)
            return queryset
        
        if id_do_usuario:
            queryset = queryset.filter(id_do_usuario=id_do_usuario)
            return queryset

        if data_de_registro:
            queryset = queryset.filter(data_de_registro=data_de_registro)
            return queryset
        return queryset



class OcupacaoViewSet(viewsets.ModelViewSet):
    queryset = Ocupacao.objects.all()
    serializer_class = OcupacaoSerializer
    permission_classes = (IsAuthenticated,)

    #Criação de filtros
    def get_queryset(self):
        queryset = Ocupacao.objects.all()
        numero = self.request.query_params.get('numero')


        if numero:
            queryset = queryset.filter(numero=numero)
            return queryset


        return queryset



class CozinhaViewSet(viewsets.ModelViewSet):
    queryset = Cozinha.objects.all()
    serializer_class = CozinhaSerializer
    permission_classes = (IsAuthenticated,)

    #Criação de filtros
    def get_queryset(self):
        queryset = Cozinha.objects.all()
        descricao = self.request.query_params.get('descricao')


        if descricao:
            queryset = queryset.filter(descricao=descricao)
            return queryset


        return queryset
