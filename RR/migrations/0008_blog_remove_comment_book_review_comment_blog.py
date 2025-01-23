# Generated by Django 5.1.5 on 2025-01-23 04:58

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("RR", "0007_comment"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("author", models.CharField(max_length=100)),
                ("date", models.DateField(default=django.utils.timezone.now)),
                ("content", models.TextField()),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="blog_images/"),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="comment",
            name="book_review",
        ),
        migrations.AddField(
            model_name="comment",
            name="blog",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="RR.blog",
            ),
        ),
    ]