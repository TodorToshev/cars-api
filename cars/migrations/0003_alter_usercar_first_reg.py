# Generated by Django 4.0.4 on 2022-04-29 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_usercar_first_reg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercar',
            name='first_reg',
            field=models.DateField(null=True),
        ),
    ]