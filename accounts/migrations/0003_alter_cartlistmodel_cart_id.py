# Generated by Django 3.2.5 on 2021-08-03 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_cartlistmodel_cart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartlistmodel',
            name='cart_id',
            field=models.CharField(max_length=250),
        ),
    ]