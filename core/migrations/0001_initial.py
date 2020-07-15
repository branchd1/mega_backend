# Generated by Django 3.0.8 on 2020-07-14 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='feature_pictures/')),
                ('community_type', models.CharField(choices=[('BAR', 'Bar')], max_length=32)),
                ('description', models.TextField()),
                ('payload', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('phone_number', models.CharField(blank=True, max_length=16, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_name', models.CharField(max_length=32)),
                ('db_pass', models.CharField(max_length=32)),
                ('db_host', models.CharField(max_length=32)),
                ('db_port', models.IntegerField()),
                ('feature', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='database', to='core.Feature')),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('type', models.CharField(choices=[('BAR', 'Bar')], max_length=32)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='community_pictures/')),
                ('description', models.TextField()),
                ('is_public', models.BooleanField()),
                ('key', models.CharField(max_length=16)),
                ('admins', models.ManyToManyField(related_name='communities_admined', to=settings.AUTH_USER_MODEL)),
                ('features', models.ManyToManyField(to='core.Feature')),
                ('members', models.ManyToManyField(related_name='communities_joined', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]