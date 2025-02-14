from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),  # Página principal que exibe a tabela de servidores
    path('login/', views.login_view, name='login'),  # Página de login
    path('lista_servidores/', views.lista_servidores, name='lista_servidores'),  # Página de lista de servidores
    path('servidores/cadastrar/', views.cadastrar_servidor, name='cadastrar_servidor'),  # Página para cadastrar um novo servidor
    path('logout/', views.logout_view, name='logout'),  # Função para fazer o logout
]

