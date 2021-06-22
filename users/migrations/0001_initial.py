# Generated by Django 3.2.4 on 2021-06-22 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=45, unique=True)),
                ('nickname', models.CharField(max_length=20, unique=True)),
                ('phone_number', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('signup_type', models.CharField(max_length=45)),
                ('profile_image', models.URLField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('options', models.ManyToManyField(through='reservations.Reservation', to='products.Option')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
