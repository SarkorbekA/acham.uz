# Generated by Django 5.0.4 on 2024-05-12 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_order_orderitem_order_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Фото коллекции'),
        ),
    ]
