from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'), 
    path('login/', views.login_view, name='login'),  
    path('lista_servidores/', views.lista_servidores, name='lista_servidores'), 
    path('servidores/cadastrar/', views.cadastrar_servidor, name='cadastrar_servidor'),
    path('servidores/editar/<int:servidor_id>/', views.editar_servidor, name='editar_servidor'),  
    path('servidores/deletar/<int:servidor_id>/', views.deletar_servidor, name='deletar_servidor'),
    path('logout/', views.logout_view, name='logout'),  
]

