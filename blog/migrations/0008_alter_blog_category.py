# Generated by Django 5.0.6 on 2024-09-30 03:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0007_alter_blog_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="category",
            field=models.CharField(
                blank=True, default="General", max_length=100, null=True
            ),
        ),
    ]
