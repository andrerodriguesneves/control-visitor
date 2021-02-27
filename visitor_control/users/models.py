from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.


class UsersManager(BaseUserManager):

    def create_user(self, email, password=None):

        users = self.model(email=self.normalize_email(email))

        users.is_active = True
        users.is_staff = False
        users.is_superuser = False

        if password:
            users.set_password(password)

        return users

    def create_superuser(self, email, password):

        users = self.create_user(email=self.normalize_email(email), password=password,)

        users.is_active = True
        users.is_staff = True
        users.is_superuser = True

        users.set_password(password)

        users.save()

        return users



class Users(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(verbose_name='E-mail do usuário', max_length=194, unique=True)    
    is_active = models.BooleanField(verbose_name='Ativo', default=True)
    is_staff = models.BooleanField(verbose_name='Desenvolvedor', default=False)
    is_superuser = models.BooleanField(verbose_name='Admin', default=False)

    USERNAME_FIELD = 'email'

    objects = UsersManager()

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

        # cria a tabela com o nome definido
        db_table = "users"

    def __str__(self):
        return self.email 