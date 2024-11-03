from django.db import models

class Department(models.Model):
    room_number = models.CharField(max_length=10, unique=True)  # 강의실 번호
    capacity = models.IntegerField()  # 수용 인원
    name = models.CharField(max_length=100)  # 학과 이름 추가 (필요 시)
    building = models.CharField(max_length=100)  # 강의실이 위치한 건물

    class Meta:
        db_table = 'department'
        verbose_name = '강의실'
        verbose_name_plural = '강의실들'  # 복수형 설정