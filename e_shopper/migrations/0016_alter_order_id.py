# Generated by Django 3.2.3 on 2022-02-03 07:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('e_shopper', '0015_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
