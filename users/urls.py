
# Django
from django.urls import path

# Views
from users import views


app_name = 'users'

urlpatterns = [
    path('registrarse/', views.SignUpView.as_view(), name='signup'),
    path('ingresar/', views.LoginViewCustom.as_view(), name='login'),
    # path('direccion/', views.AddressView.as_view(), name='address-list'),
    path('direccion/crear/', views.AddressView.as_view(), name='address-create'),
    path('salir/', views.logout_view, name='logout'),
    path('auth/login/', views.auth_login_view, name='auth_login'),
    path('callback/', views.callback_view, name='callback'),
]
