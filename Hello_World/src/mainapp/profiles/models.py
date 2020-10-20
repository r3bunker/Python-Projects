from django.db import models

# Create your models here.


PREFIX_CHOICES = {
    ('Mr.', 'Mr.'),
    ('Mrs.', 'Mrs.'),
    ('Ms.', 'Ms.'),
}


class Profiles(models.Model):
    prefix = models.CharField(
        max_length=20, default='', choices=PREFIX_CHOICES)
    firstName = models.CharField(
        max_length=20, default='', blank=True, null=False)
    lastName = models.CharField(
        max_length=20, default='', blank=True, null=False)
    email = models.CharField(max_length=60, default='', blank=True)
    username = models.CharField(max_length=30, default='', blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.firstName
