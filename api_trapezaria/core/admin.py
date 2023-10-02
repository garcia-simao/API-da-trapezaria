from django.contrib import admin
from .models import Usuario
from .models import Prato_do_dia
from .models import Funcionario
from .models import Avaliacao_de_alimento
from .models import Avaliacao_da_cozinha
from .models import Informacao_de_temperatura
from .models import Avaliacao_do_chefe
from .models import Ocupacao

admin.site.register(Usuario)
admin.site.register(Prato_do_dia)
admin.site.register(Funcionario)
admin.site.register(Avaliacao_de_alimento)
admin.site.register(Avaliacao_da_cozinha)
admin.site.register(Informacao_de_temperatura)
admin.site.register(Avaliacao_do_chefe)
admin.site.register(Ocupacao)
# Register your models here.

