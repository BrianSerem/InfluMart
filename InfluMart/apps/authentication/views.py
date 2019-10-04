from django.shortcuts import render
from rest_framework import generics

from InfluMart.apps.authentication.serializers import RegistrationSerializer


class RegistrationApiView(generics.GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        breakpoint()


