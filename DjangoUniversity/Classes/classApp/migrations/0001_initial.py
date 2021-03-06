# Generated by Django 3.1.2 on 2020-10-20 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=60)),
                ('courseNumber', models.PositiveBigIntegerField()),
                ('instructorName', models.CharField(blank=True, default='', max_length=60)),
                ('duration', models.FloatField()),
            ],
        ),
    ]
