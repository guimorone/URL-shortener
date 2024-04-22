from django.db import models
from django.utils import timezone


class UrlModel(models.Model):
    short_code = models.CharField(
        unique=True, max_length=15, verbose_name="Código curto", help_text="Máximo de 15 caracteres"
    )
    long_url = models.URLField(verbose_name="Url original")
    expiry_date = models.DateTimeField(blank=True, null=True, verbose_name="Data de validade")
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Data de criação")

    def __str__(self):
        return self.long_url

    def _has_expired(self) -> bool:
        if self.expiry_date is None:
            return False

        return self.expiry_date < timezone.now()

    has_expired = property(_has_expired)

    class Meta:
        verbose_name = 'Url'
        verbose_name_plural = 'Urls'
        db_table = 'urls'
