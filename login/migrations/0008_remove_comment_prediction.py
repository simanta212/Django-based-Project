# Generated by Django 2.2 on 2021-05-09 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20210430_2312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='prediction',
        ),
    ]