# Generated by Django 3.2.9 on 2021-11-22 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_comment_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='logo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]