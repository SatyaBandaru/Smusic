# Generated by Django 2.2.1 on 2019-11-02 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='Album_pic',
            field=models.ImageField(upload_to='media'),
        ),
    ]
