# Generated by Django 3.1.2 on 2020-10-16 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20201015_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='prefix',
            field=models.CharField(choices=[('Mrs.', 'Mrs.'), ('Mr.', 'Mr.'), ('Ms.', 'Ms.')], default='', max_length=20),
        ),
    ]
