
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken.views import obtain_auth_token

from core.views import UsuarioViewSet
from core.views import Prato_do_dia_ViewSet
from core.views import FuncionarioViewSet
from core.views import Avaliacao_de_alimentosViewSet
from core.views import Avaliacao_da_cozinhaViewSet
from core.views import Informacao_de_temperaturaViewSet
from core.views import Avaliacao_do_chefeViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = routers.DefaultRouter()
router.register(r'usuario', UsuarioViewSet)
router.register(r'pratos', Prato_do_dia_ViewSet)
router.register(r'funcionario', FuncionarioViewSet)
router.register(r'avaliacao-alimentos', Avaliacao_de_alimentosViewSet)
router.register(r'avaliacao-cozinha', Avaliacao_da_cozinhaViewSet)
router.register(r'avaliacao-chefe', Avaliacao_do_chefeViewSet)
router.register(r'informacao-temperatura', Informacao_de_temperaturaViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view())
]
