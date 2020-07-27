# Generated by Django 3.0.8 on 2020-07-25 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=16)),
                ('description', models.CharField(max_length=512)),
                ('identification', models.CharField(max_length=8, unique=True)),
                ('intdate', models.DateField()),
                ('productname', models.CharField(max_length=128)),
                ('value', models.IntegerField()),
            ],
        ),
    ]