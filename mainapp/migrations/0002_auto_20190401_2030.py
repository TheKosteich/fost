# Generated by Django 2.1.1 on 2019-04-01 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bouquet',
            name='image',
            field=models.ImageField(upload_to='bouquets'),
        ),
    ]