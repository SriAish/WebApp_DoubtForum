# Generated by Django 3.2.9 on 2021-11-26 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DoubtForum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doubtsession',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
