# Generated by Django 3.1.2 on 2020-12-14 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BestService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('logo', models.ImageField(upload_to='upload')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('main_description', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True)),
                ('more_description', models.TextField(blank=True)),
                ('logo', models.ImageField(upload_to='upload')),
                ('category', models.CharField(blank=True, max_length=300)),
                ('date', models.DateField()),
                ('is_latest', models.BooleanField(blank=True)),
                ('facebook', models.CharField(blank=True, max_length=300)),
                ('gmail', models.CharField(blank=True, max_length=300)),
                ('twitter', models.CharField(blank=True, max_length=300)),
                ('whatsapp', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('logo', models.ImageField(upload_to='upload')),
            ],
        ),
        migrations.CreateModel(
            name='Carusel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('mini_title', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('logo', models.ImageField(upload_to='upload')),
                ('status', models.IntegerField(blank=True, default=0)),
                ('rating', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ClientSays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('address', models.CharField(blank=True, max_length=300)),
                ('logo', models.ImageField(upload_to='upload')),
                ('status', models.IntegerField(blank=True, default=0)),
                ('rating', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('logo', models.ImageField(upload_to='upload')),
                ('quantities', models.IntegerField(blank=True, default=0)),
                ('status', models.IntegerField(blank=True, default=0)),
                ('rating', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('need_recovery_title', models.CharField(blank=True, max_length=300)),
                ('need_recovery_text', models.CharField(blank=True, max_length=300)),
                ('request_name', models.CharField(blank=True, max_length=300)),
                ('request_text', models.CharField(blank=True, max_length=300)),
                ('contact_address', models.CharField(blank=True, max_length=300)),
                ('phone', models.IntegerField(blank=True, default=0)),
                ('footer_theme', models.CharField(blank=True, max_length=300)),
                ('facebook', models.CharField(blank=True, max_length=300)),
                ('gmail', models.CharField(blank=True, max_length=300)),
                ('twitter', models.CharField(blank=True, max_length=300)),
                ('whatsapp', models.CharField(blank=True, max_length=300)),
                ('instagram', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('logo', models.ImageField(upload_to='upload')),
                ('old_price', models.FloatField(default=0.0)),
                ('price', models.FloatField(default=0.0)),
                ('rating', models.IntegerField(blank=True, default=0.0)),
                ('mini_description', models.CharField(blank=True, max_length=300)),
                ('description', models.CharField(blank=True, max_length=400)),
                ('is_main', models.BooleanField()),
                ('is_related', models.BooleanField()),
                ('status', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Recovery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('status', models.IntegerField(blank=True, default=0)),
                ('rating', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('mini_description', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('logo', models.ImageField(upload_to='upload')),
                ('is_main', models.BooleanField(blank=True)),
                ('status', models.IntegerField(blank=True, default=0)),
                ('rating', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('is_in_service', models.BooleanField(blank=True)),
                ('description', models.CharField(max_length=300)),
                ('logo', models.ImageField(upload_to='upload')),
                ('status', models.IntegerField(blank=True, default=0)),
                ('rating', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('is_experienced', models.BooleanField(blank=True)),
                ('logo', models.ImageField(upload_to='upload')),
                ('facebook', models.CharField(blank=True, max_length=300)),
                ('gmail', models.CharField(blank=True, max_length=300)),
                ('twitter', models.CharField(blank=True, max_length=300)),
                ('whatsapp', models.CharField(blank=True, max_length=300)),
                ('instagram', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Blogcomment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=300)),
                ('author_name', models.CharField(blank=True, max_length=300)),
                ('author_last_name', models.CharField(blank=True, max_length=300)),
                ('author_email', models.CharField(blank=True, max_length=300)),
                ('rating', models.FloatField(blank=True, default=0.0)),
                ('published_date', models.DateTimeField(blank=True)),
                ('blog', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.blog')),
            ],
        ),
    ]