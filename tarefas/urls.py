from django.urls import path
from . import views

app_name = 'tarefas'

urlpatterns = [

    path("", views.tarefas_home, name='tarefas_home'),
    path("cadastrar/", views.cadastrar_tarefa, name='cadastrar_tarefa'),
    path("remover/<int:id>/", views.remover_tarefa, name='remover_tarefa'),
    path("editar/<int:id>/", views.editar_tarefa, name='editar_tarefa'),

]