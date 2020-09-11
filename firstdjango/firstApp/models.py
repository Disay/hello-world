from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    @classmethod   #类方法
    def create(cls,name,age):
        return cls(name=name,age=age)
    class Meta:
        db_table="person"

class Student(models.Model):
    name=models.CharField(max_length=10)
    age=models.IntegerField()
    class Meta:
        db_table="Student"


class Couster(models.Model):
    phone=models.CharField(max_length=32,primary_key=True)
    token=models.CharField(max_length=128,unique=True)
    createTime=models.DateTimeField(auto_now_add=True) #设置创建时间，不会改变
    lastTime=models.DateTimeField(auto_now=True)
    isDelete=models.BooleanField(default=False)

