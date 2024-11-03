from django.urls import path
from .views.course import CourseListAPIView, CourseDetailAPIView  # course.py에서 APIView 임포트
from .views.department import DepartmentListAPIView, DepartmentDetailAPIView  # department.py에서 APIView 임포트
from .views.professor import *
from .views.student import *

urlpatterns = [
    # Course URL 패턴
    path('courses/', CourseListAPIView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),

    # Department URL 패턴
    path('departments/', DepartmentListAPIView.as_view(), name='department-list'),
    path('departments/<int:pk>/', DepartmentDetailAPIView.as_view(), name='department-detail'),

    # Student URL 패턴
    path('students/', StudentListAPIView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail'),

    # Professor URL 패턴
    path('professors/', ProfessorListAPIView.as_view(), name='professor-list'),
    path('professors/<int:pk>/', ProfessorDetailAPIView.as_view(), name='professor-detail'),
]