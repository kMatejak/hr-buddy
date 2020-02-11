from django.db import models


class Company(models.Model):
    company_name = models.TextField()
    email = models.TextField()
