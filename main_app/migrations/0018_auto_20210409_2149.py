# Generated by Django 3.1.7 on 2021-04-09 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_pill_products_routine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routine',
            name='Cleanser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.products'),
        ),
    ]
