from rest_framework import serializers

from example_app.models import Course
from example_app.models import Department
from example_app.models import Professor 
from example_app.serializers.department import DepartmentSerializer
from example_app.serializers.professor import ProfessorSerializer


class CourseSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    professor = ProfessorSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), write_only=True)
    professor_id = serializers.PrimaryKeyRelatedField(queryset=Professor.objects.all(), write_only=True)
    class Meta:
        model = Course
        fields =  '__all__'
        read_only_fields = ['id']

    def validate_course_name(self, value):
        if "badword" in value:
            raise serializers.ValidationError("Invalid course name.")
        return value

    def validate(self, data):
        if data['department'] == data['professor']:
            raise serializers.ValidationError("Department and professor cannot be the same.")
        return data