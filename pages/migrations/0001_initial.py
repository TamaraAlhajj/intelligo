# Generated by Django 2.2.5 on 2023-12-04 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComplexityPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=25)),
                ('guess', models.CharField(max_length=25)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MastersPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_a', models.CharField(max_length=5)),
                ('post_b', models.CharField(max_length=5)),
                ('post_k', models.CharField(max_length=5)),
                ('post_i', models.CharField(default=0, max_length=5)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]