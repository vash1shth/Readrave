# Generated by Django 5.1.5 on 2025-01-23 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RR', '0010_package'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default=89, upload_to='blog_images/'),
            preserve_default=False,
        ),
    ]