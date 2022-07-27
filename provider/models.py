from django.db import models

class Provider(models.Model):
    # provider_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null = True)
    cnpj = models.CharField(max_length=14, unique = True)
    telephone = models.CharField(max_length=14, null = True)

    def __str__(self):
        return self.name
