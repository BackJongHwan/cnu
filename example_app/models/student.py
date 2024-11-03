from django.db import models
from example_app.models.person import Person  # 직접 파일 경로로 임포트

class Student(Person):
    student_number = models.CharField(max_length=50,unique=True)
    year = models.IntegerField()
    grade = models.FloatField()
    major = models.CharField(max_length=50)
    class Meta:
        db_table = 'student'
        verbose_name = '학생'