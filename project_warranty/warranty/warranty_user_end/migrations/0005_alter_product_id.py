# Generated by Django 3.2.18 on 2023-05-01 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warranty_user_end', '0004_rename_product_id_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False, unique=True),
        ),
    ]