# Generated by Django 3.2.9 on 2021-11-28 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('model_id', models.PositiveBigIntegerField()),
                ('design_image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=500)),
                ('isPaid', models.BooleanField(default=False)),
                ('price', models.PositiveBigIntegerField()),
            ],
        ),
    ]
