# Generated by Django 3.1.5 on 2021-04-14 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='book_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.book'),
            preserve_default=False,
        ),
    ]
