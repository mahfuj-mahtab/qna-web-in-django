# Generated by Django 4.2.5 on 2023-09-23 15:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("cat_name", models.CharField(max_length=150)),
            ],
        ),
    ]
