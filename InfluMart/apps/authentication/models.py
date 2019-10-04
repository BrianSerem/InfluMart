from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from InfluMart.apps.helpers.models import BaseAbstractModel
# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, first_name=None, last_name=None, email=None, password=None):

        if not first_name:
            raise TypeError('Users must have a first name.')

        if not last_name:
            raise TypeError('Users must have a last name.')

        if not email:
            raise TypeError('Users must have an email address.')

        if not password:
            raise TypeError('Users must have a password.')

        user = self.model(first_name=first_name, last_name=last_name, email=self.normalize_email(
            email), username=self.normalize_email(email))
        
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, first_name=None, last_name=None, email=None, password=None):
        """Create a `User` who is also a superuser"""
        if not first_name:
            raise TypeError('Superusers must have a first name.')

        if not last_name:
            raise TypeError('Superusers must have a last name.')

        if not email:
            raise TypeError('Superusers must have an email address.')

        if not password:
            raise TypeError('Superusers must have a password.')

        user = self.model(
            first_name=first_name, last_name=last_name,
            email=self.normalize_email(email))
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.is_verified = True
        user.set_password(password)
        user.save()

class User(AbstractUser, BaseAbstractModel):

    USER_ROLES = (
        ('BS', 'BUYER-SELLER'),
        ('ADM', 'ADMIN'),
    )

    role = models.CharField(verbose_name = 'user role', default='BS', max_length=3, choices=USER_ROLES)



