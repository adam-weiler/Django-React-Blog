# Generated by Django 2.2.3 on 2019-07-29 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190728_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]