# models/course.py
from django.db import models

from .professor import Professor  # 직접 임포트
from .student import Student  # 직접 임포트
from .department import Department  # 직접 임포트

class Course(models.Model):
    course_name = models.CharField(max_length=20, unique=True)  # 과목 번호
    professor = models.ForeignKey("example_app.professor", on_delete=models.CASCADE)  # 교수와 연결
    section = models.IntegerField()  # 분반
    credits = models.IntegerField()  # 학점
    department = models.ForeignKey("example_app.department", on_delete=models.CASCADE)  # 강의실과 연결
    max_students = models.IntegerField()  # 최대 정원
    year = models.IntegerField()  # 수업 년도
    semester = models.CharField(max_length=10)  # 학기 (예: 'Spring', 'Fall')
    syllabus = models.TextField()  # 강의 계획서

    class Meta:
        db_table = 'course'
        verbose_name = '과목'