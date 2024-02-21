# Generated by Django 4.2.9 on 2024-02-21 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('frontend', 'FrontEnd'), ('backend', 'BackEnd'), ('digital marketing', 'Digital Marketing'), ('technological reports', 'Technological Reports'), ('entertainment', 'Entertainment')], default='unknown', max_length=50)),
                ('published', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]