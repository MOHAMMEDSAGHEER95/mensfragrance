from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class DateTimeBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Perfume(DateTimeBase):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    image = models.ImageField()
    cost = models.CharField(max_length=30)
    
    class Meta:
        verbose_name = _('Perfume')
        verbose_name_plural = _('Perfumes')

    def __str__(self):
        return self.name


