# Generated by Django 4.2.5 on 2023-10-06 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciepe_model',
            name='image',
            field=models.ImageField(default='E:/personal/django_practic/recipy/mainapp/image/', upload_to=''),
        ),
    ]
