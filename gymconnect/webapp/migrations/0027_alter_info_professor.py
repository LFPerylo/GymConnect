# Generated by Django 5.0.4 on 2024-05-27 19:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0026_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.dados'),
        ),
    ]
