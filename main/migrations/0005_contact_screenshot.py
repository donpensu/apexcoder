# Generated by Django 4.2.3 on 2023-07-12 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='screenshot',
            field=models.ImageField(default='img/emma.jpg', upload_to='screenshot'),
        ),
    ]