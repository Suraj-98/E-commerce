# Generated by Django 3.2.3 on 2022-01-28 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_shopper', '0010_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.FloatField(null=True),
        ),
    ]
