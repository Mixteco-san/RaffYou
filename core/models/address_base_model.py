
# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Models
from core.models import BaseModel

# Utilities
from core.utils import clean_word


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
            f'*Solicitante:* {clean_word(self.name)}\n'
            f'*Calle:* {clean_word(self.street_name)}\n'
            f'*Número:* {clean_word(self.street_number)}\n'
            f'*Barrio:* {clean_word(self.colony)}\n'
            f'*Teléfono:* {clean_word(self.telephone)}\n'
            f'*Notas:* {clean_word(self.references)}\n'
        )

    @property
    def clean_telephone(self):
        return self.telephone.replace(' ', '').strip()

    def __str__(self):
        return f'{self.user} - {self.zip_code}'

    class Meta:
        abstract = True
