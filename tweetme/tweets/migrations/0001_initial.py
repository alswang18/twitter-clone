# Generated by Django 3.1.4 on 2021-01-01 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.FileField(blank=True, upload_to='images/')),
            ],
        ),
    ]