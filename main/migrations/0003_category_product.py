# Generated by Django 4.2.3 on 2023-07-05 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_delete_apprash'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('catslug', models.SlugField(unique=True)),
                ('catimg', models.ImageField(upload_to='catimg')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True)),
                ('pix', models.ImageField(upload_to='pix')),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('promo_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('topselling', models.BooleanField()),
                ('featured', models.BooleanField()),
                ('upload', models.DateField(auto_now=True)),
                ('edited', models.DateField(auto_now_add=True)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
        ),
    ]