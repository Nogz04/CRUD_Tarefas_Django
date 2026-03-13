from django.db import models

class TarefaModel(models.Model):

    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    concluida = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True) # quando o registro for criado, já registra a data/horario de criação


    # Quando a tarefa for estanciada, o nome dela aparece.
    def __str__(self):
        return self.nome