from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


# Model for the Roleplay itself
# Needs to have a title and a description
# will be used to organize related posts, characters and maybe locations
class RolePlay(models.Model):
    title = models.CharField(verbose_name="Title",
                             max_length=1024)
    description = CKEditor5Field(verbose_name="Description")

    class Meta:
        verbose_name = "Roleplay"
        verbose_name_plural = "Roleplays"

    def __str__(self):
        return f"Roleplay: {self.title}"
