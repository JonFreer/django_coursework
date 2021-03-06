# Generated by Django 2.2.15 on 2020-08-21 14:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0006_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang_id', models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('experience', models.CharField(max_length=20)),
            ],
        ),
    ]
