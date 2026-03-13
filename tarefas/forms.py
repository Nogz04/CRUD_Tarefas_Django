from django import forms

from tarefas.models import TarefaModel

class TarefaForm(forms.ModelForm):
    # Classe Meta é uma classe interna que serve para configurar o formulário, dizendo qual modelo ele vai usar e quais campos do modelo ele vai usar.
    class Meta:
        model = TarefaModel # Model que vai ser utilizado para esse formulário
        fields = ['nome', 'descricao', 'concluida'] # Campos do modelo que vão ser utilizados no formulário. Se quiser usar todos os campos, pode usar fields = '__all__' ou excluir o atributo fields.
        