from django.contrib import admin
from .models import Usuario
from .models import Prato_do_dia
from .models import Funcionario
from .models import Avaliacao_de_alimentos
from .models import Avaliacao_da_cozinha
from .models import Infomacao_de_tempetatura
from .models import Avaliacao_do_chefe

admin.site.register(Usuario)
admin.site.register(Prato_do_dia)
admin.site.register(Funcionario)
admin.site.register(Avaliacao_de_alimentos)
admin.site.register(Avaliacao_da_cozinha)
admin.site.register(Infomacao_de_tempetatura)
admin.site.register(Avaliacao_do_chefe)
# Register your models here.

