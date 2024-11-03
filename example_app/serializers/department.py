from rest_framework import serializers

from example_app.models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department 
        fields = '__all__'
        read_only_fields = ['id']
    def validate_course_name(self, value):
        if "badword" in value:
            raise serializers.ValidationError("Invalid department name.")
        return value