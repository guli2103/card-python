# Generated by Django 4.1.3 on 2022-12-14 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_mainpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rangi', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='mainpost',
            name='content',
            field=models.TextField(verbose_name="Ma'lumot"),
        ),
        migrations.AlterField(
            model_name='mainpost',
            name='img',
            field=models.CharField(max_length=255, verbose_name='Rasm'),
        ),
        migrations.AlterField(
            model_name='mainpost',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Ism'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name="Ma'lumot"),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Sana'),
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.CharField(max_length=255, verbose_name='Rasm'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Ism'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tanlov',
            field=models.CharField(max_length=20, verbose_name='Tanlov'),
        ),
        migrations.AlterField(
            model_name='toppost',
            name='content',
            field=models.TextField(verbose_name="Ma'lumot"),
        ),
        migrations.AlterField(
            model_name='toppost',
            name='data',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Sana'),
        ),
        migrations.AlterField(
            model_name='toppost',
            name='img',
            field=models.CharField(max_length=255, verbose_name='Rasm'),
        ),
        migrations.AlterField(
            model_name='toppost',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Ism'),
        ),
        migrations.AlterField(
            model_name='toppost',
            name='tanlov',
            field=models.CharField(max_length=20, verbose_name='Tanlov'),
        ),
        migrations.CreateModel(
            name='Moshin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=255)),
                ('rangi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.rang')),
            ],
        ),
    ]
