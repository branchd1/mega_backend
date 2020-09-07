# Generated by Django 3.0.8 on 2020-09-07 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('picture', models.ImageField(upload_to='community_pictures/')),
                ('description', models.TextField(default='')),
                ('key', models.CharField(max_length=10, unique=True)),
                ('admins', models.ManyToManyField(blank=True, related_name='communities_admined', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'communities',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CommunityType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('picture', models.ImageField(upload_to='feature_pictures/')),
                ('description', models.TextField()),
                ('key', models.CharField(max_length=10, unique=True)),
                ('payload', models.TextField()),
                ('approved', models.NullBooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='UploadedImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='features/')),
            ],
        ),
        migrations.CreateModel(
            name='SimpleStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=128)),
                ('value', jsonfield.fields.JSONField(default=dict)),
                ('access', models.CharField(choices=[('PUBL', 'Public'), ('USER', 'User'), ('ADMN', 'Admin')], max_length=32)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='simple_store', to='core.Community')),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='simple_store', to='core.Feature')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='simple_store', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.AddField(
            model_name='community',
            name='features',
            field=models.ManyToManyField(blank=True, related_name='communities_using', to='core.Feature'),
        ),
        migrations.AddField(
            model_name='community',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='communities_joined', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='community',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='communities_with_type', to='core.CommunityType'),
        ),
    ]
