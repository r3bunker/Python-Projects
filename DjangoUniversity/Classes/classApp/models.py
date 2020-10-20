from django.db import models

# Create your models here.


class djangoClasses(models.Model):
    title = models.CharField(max_length=60, default='')
    courseNumber = models.PositiveBigIntegerField()
    instructorName = models.CharField(
        max_length=60, default='', blank=True, null=False)
    duration = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return self.title
