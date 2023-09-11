from rest_framework import serializers
from .models import Usuario
from .models import Prato_do_dia
from .models import Funcionario
from .models import Avaliacao_de_alimentos
from .models import Avaliacao_da_cozinha
from .models import Infomacao_de_tempetatura

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'codigo_entrada', 'nome', 'email', 'username','password','departamento','observacao','data_de_registro']


class Prato_do_dia_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Prato_do_dia
        fields = ['id', 'nome_do_prato', 'descricao', 'chefe','imagem','caloria','data_refeicao','data_de_registro']


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['id', 'nome', 'email', 'Numero_do_bilhete','funcao','departamento','permissao','endereco','data_de_registro']


class Avaliacao_de_alimentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao_de_alimentos
        fields = ['id', 'id_do_prato', 'numero_de_estrelas', 'id_do_usuario','data_de_registro']


class Avaliacao_da_cozinhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao_da_cozinha
        fields = ['id', 'numero_de_estrelas', 'id_do_usuario','data_de_registro']

class Informacao_de_temperaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infomacao_de_tempetatura
        fields = ['id', 'temperatura_ambiental', 'temperatura_do_contentor','data_de_registro']



