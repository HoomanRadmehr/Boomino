from django.db import models

class History(models.Model):
    a=models.IntegerField()
    b=models.IntegerField()

    def __str__(self) -> str:
        return f'{self.a} - {self.b}'
        