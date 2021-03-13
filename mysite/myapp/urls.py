from django.urls import path
from .views import base, form_view, okay, fail, login


urlpatterns = [
    # path('', base, name='base'),
    path('', form_view, name='form-view'),
    path('okay/', okay, name='okay'),
    path('fail/', fail, name='fail'),
    path('login/', login, name='login')
]
