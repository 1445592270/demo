# Generated by Django 2.2.1 on 2019-09-11 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_auto_20190911_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=32, verbose_name='书名'),
        ),
        migrations.AlterField(
            model_name='book',
            name='p',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Publish', verbose_name='外键'),
        ),
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateField(auto_now=True, null=True, verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='person',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='身高'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=32, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='publish',
            name='address',
            field=models.CharField(max_length=32, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='publish',
            name='name',
            field=models.CharField(max_length=32, verbose_name='出版社'),
        ),
    ]