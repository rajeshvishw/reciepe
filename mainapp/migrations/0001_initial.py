# Generated by Django 4.2.5 on 2023-10-06 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reciepe_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]