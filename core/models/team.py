from django.db import models

from utils.model import Model
from django_extensions.db.models import ActivatorModel, TimeStampedModel, TitleSlugDescriptionModel
from ckeditor.fields import RichTextField

class Team(ActivatorModel, TimeStampedModel, TitleSlugDescriptionModel, Model):
    class Meta:
        verbose_name_plural = "Team members"

