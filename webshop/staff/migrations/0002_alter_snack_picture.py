# Generated by Django 4.2.4 on 2023-08-13 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snack',
            name='picture',
            field=models.ImageField(null=True, upload_to='files/images/'),
        ),
    ]
