# Generated by Django 4.2.5 on 2023-10-06 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_reciepe_model_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciepe_model',
            name='image',
            field=models.ImageField(upload_to='E:/personal/django_practic/recipy/mainapp/image/'),
        ),
    ]