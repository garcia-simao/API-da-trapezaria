from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User, weak=False)
def report_uploaded(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)




#Criacao dos modelos
class Usuario(models.Model):
    codigo_entrada = models.IntegerField()
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)
    observacao = models.CharField(max_length=50)
    data_de_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome






class Funcionario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    Numero_do_bilhete = models.CharField(max_length=50)
    funcao = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='')
    departamento = models.CharField(max_length=50)
    permissao = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    data_de_registro = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nome
    



class Prato_do_dia(models.Model):
    nome_do_prato = models.CharField(max_length=50)
    descricao = models.CharField(max_length=500)
    chefe = models.ForeignKey(Funcionario, on_delete=models.PROTECT, related_name="funcionarios" )
    imagem = models.ImageField(upload_to='')
    caloria = models.FloatField()
    data_refeicao = models.DateTimeField()
    data_de_registro = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.nome_do_prato
    





class Avaliacao_de_alimento(models.Model):
    id_do_prato = models.ForeignKey(Prato_do_dia, on_delete=models.PROTECT, related_name="pratos")
    numero_de_estrelas = models.IntegerField()
    id_do_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="usuario")
    data_de_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.numero_de_estrelas)


class Avaliacao_da_cozinha(models.Model):
    numero_de_estrelas = models.IntegerField()
    id_do_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name="usuarios")
    data_de_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.numero_de_estrelas)
    


class Informacao_de_temperatura(models.Model):
    temperatura_ambiental = models.FloatField()
    temperatura_do_contentor = models.FloatField()
    data_de_registro = models.DateTimeField(auto_now_add=True)
    
   
    def __str__(self):
        return str(self.temperatura_ambiental)
    

class Avaliacao_do_chefe(models.Model):
    id_do_chefe = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    id_do_usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT )
    numero_de_estrelas = models.IntegerField()
    data_de_registro = models.DateTimeField(auto_now_add=True)
    
   
    def __str__(self):
        return str(self.id_do_chefe)



    