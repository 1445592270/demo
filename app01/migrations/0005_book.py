# Generated by Django 2.2.1 on 2019-09-11 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20190911_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Publish')),
            ],
        ),
    ]
