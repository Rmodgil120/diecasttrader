# Generated by Django 4.2.4 on 2023-08-17 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_tomica_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='maisto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('image_url', models.CharField(max_length=2083)),
            ],
        ),
    ]
