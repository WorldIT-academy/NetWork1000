# Generated by Django 5.1.4 on 2025-03-01 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='icon',
            field=models.ImageField(blank=True, upload_to='images/tag_icons'),
        ),
        migrations.AddField(
            model_name='tag',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
