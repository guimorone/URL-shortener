from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string


class UrlModel(models.Model):
    long_url = models.URLField(primary_key=True, verbose_name="Url original")
    short_code = models.CharField(
        unique=True, max_length=15, verbose_name="Código curto", help_text="Máximo de 15 caracteres"
    )
    expiry_date = models.DateTimeField(blank=True, null=True, verbose_name="Data de validade")
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Data de criação")

    def __str__(self):
        return self.short_code

    def _has_expired(self) -> bool:
        if self.expiry_date is None:
            return False

        return self.expiry_date < timezone.now()

    has_expired = property(_has_expired)

    def save(self, *args, **kwargs) -> None:
        if not self.short_code:
            self.short_code = get_random_string(10)

        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Url'
        verbose_name_plural = 'Urls'
        db_table = 'urls'
