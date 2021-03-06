# Generated by Django 3.2.3 on 2022-01-11 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_shopper', '0002_userdetails_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='updateprofileimage',
            name='address',
        ),
        migrations.RemoveField(
            model_name='updateprofileimage',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='updateprofileimage',
            name='mobile_no',
        ),
        migrations.RemoveField(
            model_name='updateprofileimage',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='userdetails',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='mobile',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='zip',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
