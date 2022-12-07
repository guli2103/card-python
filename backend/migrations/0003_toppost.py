# Generated by Django 3.2 on 2022-12-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_post_content_post_date_post_name_post_tanlov'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('tanlov', models.CharField(max_length=20)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('img', models.CharField(max_length=255)),
            ],
        ),
    ]