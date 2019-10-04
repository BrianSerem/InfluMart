from django.urls import path

from InfluMart.apps.authentication.views import RegistrationApiView

app_name = 'authentication'

urlpatterns = [
   path('register/', RegistrationApiView.as_view(), name='register' )
]

