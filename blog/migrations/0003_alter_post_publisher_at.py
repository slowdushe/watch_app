# Generated by Django 5.0.1 on 2024-02-08 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_publisher_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publisher_at',
            field=models.DateField(),
        ),
    ]
