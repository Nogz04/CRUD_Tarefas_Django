from django.shortcuts import render, redirect, get_object_or_404
from .forms import TarefaForm
from .models import TarefaModel
from django.http import HttpRequest

def tarefas_home(request):

    contexto = {

        "nome":"Matheus",
        "tarefas":TarefaModel.objects.all() # TarefaModel.objects.all() é uma consulta ao banco de dados que retorna todos os registros da tabela de tarefas, ou seja, todas as tarefas cadastradas. O resultado dessa consulta é uma lista de objetos do tipo TarefaModel, que podem ser usados para exibir as informações das tarefas na página.

    }

    return render(request, 'tarefas/home.html', contexto)

def cadastrar_tarefa(request: HttpRequest):

    if request.method == 'POST':
        formulario = TarefaForm(request.POST) # Fomulario recebe os dados do formulário preenchido pelo usuário, que estão em request.POST
        if formulario.is_valid(): # Verifica se o formulário é válido, ou seja, se os dados estão corretos e podem ser salvos no banco de dados.
            formulario.save() # Salva os dados do formulário no banco de dados, criando um novo registro na tabela de tarefas.
            return redirect('tarefas:tarefas_home') # Redireciona o usuário para a página de tarefas, onde ele pode ver a lista de tarefas cadastradas.

    contexto = {

        "form": TarefaForm()

    }

    return render(request, 'tarefas/cadastrar_tarefa.html', contexto)


def remover_tarefa(request: HttpRequest, id: int):
    tarefa = get_object_or_404(TarefaModel, id=id) # get_object_or_404 é uma função do Django que tenta obter um objeto do banco de dados com base em um modelo e um identificador. Se o objeto for encontrado, ele é retornado. Caso contrário, a função gera uma resposta HTTP 404 (Not Found), indicando que o recurso solicitado não foi encontrado.
    tarefa.delete()
    return redirect('tarefas:tarefas_home')


def editar_tarefa(request: HttpRequest, id: int):

    tarefa = get_object_or_404(TarefaModel, id=id)

    if request.method == 'POST':
        formulario = TarefaForm(request.POST, instance=tarefa) # O parâmetro instance=tarefa é usado para preencher o formulário com os dados da tarefa existente, permitindo que o usuário edite as informações. Se request.POST estiver vazio (ou seja, se for uma requisição GET), o formulário será preenchido com os dados atuais da tarefa. Se request.POST contiver dados (ou seja, se for uma requisição POST), o formulário será preenchido com os dados enviados pelo usuário, mas ainda estará associado à tarefa existente.
        if formulario.is_valid():
            formulario.save() # Salva as alterações feitas no formulário, atualizando o registro da tarefa existente no banco de dados.
            return redirect('tarefas:tarefas_home')    

    formulario = TarefaForm(request.POST or None, instance=tarefa) # O parâmetro instance=tarefa é usado para preencher o formulário com os dados da tarefa existente, permitindo que o usuário edite as informações. Se request.POST estiver vazio (ou seja, se for uma requisição GET), o formulário será preenchido com os dados atuais da tarefa. Se request.POST contiver dados (ou seja, se for uma requisição POST), o formulário será preenchido com os dados enviados pelo usuário, mas ainda estará associado à tarefa existente.

    contexto = {

        "form": formulario

    }



    return render(request, 'tarefas/editar_tarefa.html', contexto)

