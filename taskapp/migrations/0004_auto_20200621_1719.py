# Generated by Django 2.1 on 2020-06-21 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0003_auto_20200621_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='img',
            field=models.FileField(default=None, upload_to='pic/'),
        ),
    ]