# Generated by Django 3.1.2 on 2020-10-16 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, default='', max_length=20)),
                ('lastName', models.CharField(blank=True, default='', max_length=20)),
                ('email', models.CharField(blank=True, default='', max_length=60)),
                ('username', models.CharField(blank=True, default='', max_length=30)),
            ],
        ),
    ]
