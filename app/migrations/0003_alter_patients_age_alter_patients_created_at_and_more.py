# Generated by Django 4.0.6 on 2022-08-20 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_patients_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='age',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='email',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]