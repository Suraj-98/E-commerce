# Generated by Django 3.2.3 on 2022-02-02 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_shopper', '0013_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
