# Generated by Django 4.2 on 2023-04-10 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
