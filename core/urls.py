from django.urls import path
from .views import Index, Cadastro, Logar, sair, CreateProdutoView, UpdateProdutoView, DeleteProdutoView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('cadastro/', Cadastro.as_view(), name='cadastro'),
    path('logar/', Logar.as_view(), name='logar'),
    path('deslogar', sair),
    path('add/', CreateProdutoView.as_view(), name='add_produto'),
    path('<int:pk>/update/', UpdateProdutoView.as_view(), name='upd_produto'),
    path('<int:pk>/delete/', DeleteProdutoView.as_view(), name='del_produto'),
]