# Generated by Django 4.0.6 on 2022-08-20 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_patients_age_alter_patients_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='patients',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
