# Generated by Django 3.2.9 on 2021-11-11 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts', verbose_name='image')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]