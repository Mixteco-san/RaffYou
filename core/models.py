
# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    """Products base model"""
    created_at = models.DateTimeField(
        _('Fecha de creación'),
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        _('Fecha de modificación'),
        auto_now=True
    )

    class Meta:
        abstract = True


class CatalogModelBase(BaseModel):
    """Catalog model base"""
    code = models.CharField(
        _('Código'),
        max_length=30,
        unique=True
    )
    value = models.CharField(
        _('Nombre'),
        max_length=100
    )

    description = models.CharField(
        _('Descripción'),
        max_length=250,
        blank=True
    )

    def __str__(self):
        return '{} - {}'.format(self.code, self.value)

    class Meta:
        abstract = True


class AddressBaseModel(BaseModel):

    name = models.CharField(
        _('Nombre y apellido'),
        max_length=250
    )

    zip_code = models.CharField(
        _('Código postal'),
        max_length=10
    )

    state = models.CharField(
        _('Estado'),
        max_length=50
    )

    city = models.CharField(
        _('Delegación / Municipio'),
        max_length=255
    )

    colony = models.CharField(
        _('Barrio / Colonia / Asentamiento'),
        max_length=255
    )

    street_name = models.CharField(
        _('Calle'),
        max_length=255
    )

    street_number = models.CharField(
        _('N° Exterior'),
        max_length=10
    )

    internal_number = models.CharField(
        _('N° Interior / Depto (opcional)'),
        max_length=10,
        blank=True
    )

    between_street1 = models.CharField(
        _('Calle 1'),
        max_length=255,
        blank=True
    )

    between_street2 = models.CharField(
        _('Calle 2'),
        max_length=255,
        blank=True
    )

    telephone = models.CharField(
        _('Teléfono de contacto'),
        max_length=20,
    )

    references = models.TextField(
        _('Ayuda al repartido a encontrar tu domicilio o el producto que necesitas'),
        max_length=500
    )

    @property
    def full_address(self):
        return (
            f'*Calle:* {self.street_name}\n'
            f'*Número:* {self.street_number}\n'
            f'*Barrio:* {self.colony}\n'
            f'*A la persona:* {self.name}\n'
            f'*Teléfono:* {self.telephone}\n'
            f'*Notas:* {self.references}\n'
        )

    def __str__(self):
        return f'{self.user} - {self.zip_code}'

    class Meta:
        abstract = True
