from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager # Importa el manager personalizado

class Perfil(models.Model):
    perfil_id = models.IntegerField(primary_key=True)
    perfil_nombre = models.CharField(max_length=100, null=False)
    def __str__(self):
        return f'{self.perfil_id}: {self.perfil_nombre}'
    class Meta:
        db_table = 'perfiles'

class Usuario(AbstractUser):
   # Se elimina 'username' porque ya existe en AbstractUser
   full_name = models.CharField(max_length=100, null=False, blank=False)
   email = models.EmailField(null=False, unique=True)
   mobile = models.CharField(max_length=15, blank=True)
   perfil = models.ForeignKey(Perfil, null=True, on_delete=models.RESTRICT, related_name="perfiles_usuarios")

   # Asigna el manager personalizado
   objects = UserManager()

   # USERNAME_FIELD ya está definido como 'username' en AbstractUser
   REQUIRED_FIELDS = ['full_name', 'email']

   class Meta:
       db_table = "usuarios"

   def __str__(self):
       return self.full_name


