# Generated by Django 3.0.6 on 2020-06-20 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_scheduleday'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='order',
            field=models.IntegerField(default=1, verbose_name='Orden en el que deberían aparecer los productos en el home'),
        ),
    ]
