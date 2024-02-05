from django.db import models

from config import settings
from users.models import NULLABLE


class Client(models.Model):
    email = models.EmailField(verbose_name='Contact email')
    name = models.CharField(max_length=100, verbose_name='Name')
    comment = models.CharField(max_length=255, **NULLABLE, verbose_name='Comment')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                              related_name='cleints', related_query_name='client',
                              **NULLABLE, verbose_name='Mailing_List_Owner')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'MailingClient'
        verbose_name_plural = 'MailingClients'
        ordering = ('email',)
