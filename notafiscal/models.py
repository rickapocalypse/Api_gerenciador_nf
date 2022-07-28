from django.db import models
from provider.models import Provider

class NotaFiscal(models.Model):

    STATUS = (
        ('1', 'não pago'),
        ('2', 'pago'),
    )

    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True)
    number = models.IntegerField()
    data = models.DateField(auto_now=True)
    name_product = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_valor = models.DecimalField(max_digits=10, decimal_places=2)
    payment = models.CharField(max_length=1, choices=STATUS)

    def __str__(self):
        return self.name_product
    class Meta:
        verbose_name = 'Nota Fiscal'
        verbose_name_plural = 'Notas Fiscais'
        ordering = ['data']