# Generated by Django 4.1.5 on 2023-01-25 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='news/', verbose_name='Image'),
        ),
    ]
