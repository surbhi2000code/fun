# Generated by Django 3.1.5 on 2021-01-26 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lol', '0002_auto_20210113_2340'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('mobile', models.CharField(default='', max_length=505)),
                ('desc', models.CharField(max_length=700)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.CharField(default='', max_length=505),
        ),
    ]
