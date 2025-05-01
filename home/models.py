from django.db import models

class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    nome          = models.TextField()
    comentario    = models.TextField()

    def __str__(self):
        return f"Nome: {self.nome} | Comentário: {self.comentario}"
        
