# Generated by Django 3.1 on 2022-02-02 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.TextField()),
                ('cover', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
