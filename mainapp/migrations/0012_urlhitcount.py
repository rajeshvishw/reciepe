# Generated by Django 4.2.5 on 2023-10-09 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_alter_reciepe_model_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='URLHitCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255, unique=True)),
                ('hit_count', models.IntegerField(default=0)),
            ],
        ),
    ]
