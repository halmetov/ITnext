# Generated by Django 3.1.2 on 2020-12-24 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20201224_1037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcomment',
            old_name='published_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='blogcomment',
            old_name='author_email',
            new_name='email',
        ),
    ]