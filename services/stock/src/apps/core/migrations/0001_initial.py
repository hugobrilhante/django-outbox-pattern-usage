# Generated by Django 4.2.8 on 2024-01-19 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=20)),
                ('product_id', models.CharField(max_length=20)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(choices=[('reserved', 'Reserved'), ('not_reserved', 'Not Reserved'), ("payment_denied", "Payment Denied")], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=20)),
                ('quantity', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]