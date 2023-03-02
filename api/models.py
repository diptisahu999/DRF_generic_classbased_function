from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    mobile=models.IntegerField(max_length=10)
    password=models.CharField(max_length=5)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='student_table'
