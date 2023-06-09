# Generated by Django 3.2.18 on 2023-04-30 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=200)),
                ('Description', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('warranty_period', models.IntegerField()),
                ('brought_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_time', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
