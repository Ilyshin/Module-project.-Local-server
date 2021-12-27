# Generated by Django 4.0 on 2021-12-26 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('birthday', models.DateField(verbose_name='birthday')),
                ('nationality', models.IntegerField(choices=[(3, 'ger'), (2, 'fr'), (1, 'rus'), (4, 'eng'), (5, 'esp')], verbose_name='nationality')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='User')),
            ],
        ),
    ]
