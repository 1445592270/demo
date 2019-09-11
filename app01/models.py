from django.db import models

# Create your models here.


class Person(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32,verbose_name='姓名')
    age=models.IntegerField(verbose_name='年龄')
    height=models.DecimalField(max_digits=5,decimal_places=2,verbose_name='身高')
    birthday=models.DateField(null=True,auto_now=True,verbose_name='生日')

    def __str__(self):
        return self.name
    class Meta:
        db_table='person'

class Publish(models.Model):
    name=models.CharField(max_length=32,verbose_name='出版社')
    address=models.CharField(max_length=32,verbose_name='地址')
    def __str__(self):
        return self.name
    class Meta:
        db_table='publish'
class Book(models.Model):
    name=models.CharField(max_length=32,verbose_name='书名')
    p=models.ForeignKey(to=Publish,to_field='id',on_delete=models.CASCADE,verbose_name='外键')
    def __str__(self):
        return self.name
    class Meta:
        db_table='book'