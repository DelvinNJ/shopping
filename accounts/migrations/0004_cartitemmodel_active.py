# Generated by Django 3.2.5 on 2021-08-03 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_cartlistmodel_cart_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitemmodel',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]