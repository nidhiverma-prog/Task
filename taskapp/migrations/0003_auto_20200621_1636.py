# Generated by Django 2.1 on 2020-06-21 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0002_auto_20200621_1626'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AlterField(
            model_name='employee',
            name='img',
            field=models.FileField(default=None, upload_to='media/pic/'),
        ),
    ]
