
# Django
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

# Models
from users.models import Address

# Forms
from users.forms import AddressForm


class AddressUpdateView(UpdateView):
    template_name = 'users/address.html'
    form_class = AddressForm
    success_url = reverse_lazy('users:address-list')

    def get_queryset(self):
        return Address.objects.filter(
            user=self.request.user
        )
