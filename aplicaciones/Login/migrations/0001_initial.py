# Generated by Django 5.1.3 on 2024-12-06 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('correo', models.EmailField(max_length=254)),
                ('contra', models.CharField(max_length=100)),
            ],
        ),
    ]
