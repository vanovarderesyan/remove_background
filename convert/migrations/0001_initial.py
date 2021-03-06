# Generated by Django 3.2.4 on 2021-06-28 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Convert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('path', models.ImageField(upload_to='')),
                ('status', models.CharField(blank=True, choices=[('start', 'start'), ('failed', 'failed'), ('completed', 'completed')], max_length=30, null=True)),
                ('file_name', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
