from django.db import models


# Create your models here.


class Offers(models.Model):
    company_name = models.TextField()
    company_mail = models.TextField()
