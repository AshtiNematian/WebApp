# Generated by Django 4.2.9 on 2024-02-21 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('picture', models.ImageField(upload_to='Images')),
                ('description', models.TextField()),
                ('published', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
    ]
