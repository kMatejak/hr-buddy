from django.db import models


# Create your models here.
class Application(models.Model):
    FullName = models.TextField()
    Email = models.TextField()
    Phone = models.TextField()
    Location = models.TextField()
    Education = models.TextField()
    Publications = models.TextField()
    languages = models.TextField()
    references = models.TextField()
