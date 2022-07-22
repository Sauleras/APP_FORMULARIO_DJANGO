from django.urls import path
from .views import Index, Cadastro, Logar

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('cadastro/', Cadastro.as_view(), name='cadastro'),
    path('logar/', Logar.as_view(), name='logar'),
]