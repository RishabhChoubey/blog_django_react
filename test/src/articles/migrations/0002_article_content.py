# Generated by Django 3.0.2 on 2020-01-20 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default='cool!!!'),
        ),
    ]