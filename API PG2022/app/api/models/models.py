from django.db import models
from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)

from django_currentuser.db.models import CurrentUserField


class AbstarctModel(models.Model):
    # Set some fields here
    

    class Meta:
        abstract = True

class ControlModel(models.Model):
    created_at = models.DateField(("Criado em"), auto_now_add=True, null=True)
    updated_at = models.DateField(("Actualizado em"), auto_now=True, null=True)
    created_by = CurrentUserField(related_name='created_%(class)ss', null=True)
    updated_by = CurrentUserField(related_name='updated_%(class)ss', null=True)
    

    class Meta:
       abstract = True

