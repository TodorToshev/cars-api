# Generated by Django 4.0.4 on 2022-04-29 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_rename_model_name_carmodel_car_model_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='car_brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='model_brand', to='cars.carbrand'),
        ),
    ]