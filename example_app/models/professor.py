from django.db import models
from example_app.models.person import Person  # 직접 파일 경로로 임포트

class Professor(Person):
    contact = models.CharField(max_length=50)

    class Meta:
        db_table = 'professor'
        verbose_name = '교수'