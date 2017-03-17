# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 00:29
from __future__ import unicode_literals

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
            name='IssueAlreadyCommented',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=256)),
                ('owner_type', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=256)),
                ('gh_id', models.CharField(max_length=32)),
                ('creationDate', models.DateTimeField()),
                ('createdByUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserRepoConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_links', models.BooleanField()),
                ('new_only', models.BooleanField()),
                ('creationDate', models.DateTimeField()),
                ('last_ran', models.DateTimeField()),
                ('already_did_old', models.BooleanField()),
                ('repo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gh_frespo_integration.Repo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='issuealreadycommented',
            name='repo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gh_frespo_integration.Repo'),
        ),
    ]
