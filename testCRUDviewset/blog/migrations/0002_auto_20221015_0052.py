# Generated by Django 3.2.16 on 2022-10-14 19:52

from django.db import migrations


def fill_preform_data(apps, schema_editor):
    fill_users(apps)


def fill_users(apps):
    User = apps.get_model('blog', 'User')
    User.objects.create(name="Алексей")
    User.objects.create(name="Александр")
    User.objects.create(name="Андрей")
    User.objects.create(name="Альберт")


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(fill_preform_data),
    ]