# Generated by Django 3.1.2 on 2020-10-16 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20201015_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='prefix',
            field=models.CharField(choices=[('Ms.', 'Ms.'), ('Mrs.', 'Mrs.'), ('Mr.', 'Mr.')], default='', max_length=20),
        ),
    ]
