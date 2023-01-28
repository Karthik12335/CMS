from  rest_framework import serializers

from .models import Class,Course,Student,Subject,Teacher

class CourseSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source="name")
    class Meta:
        model = Course
        fields = ["id","course_name"]

class SubjectSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    class Meta:
        model = Subject
        fields = ["id","name","course"]

   
    

class StudentSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    class Meta:
        model = Student
        fields = ["id","name","student_id","course"]

class TeacherSerializer(serializers.ModelSerializer):
    subjects = serializers.SerializerMethodField()
    class Meta:
        model = Teacher
        fields = ["id","name","subjects"]

    def get_subjects(self, obj):
        return [s.name for s in obj.subjects.all()]

class ClassSerializer(serializers.ModelSerializer):
    
    subject = SubjectSerializer()
    teacher = TeacherSerializer()
    students = StudentSerializer(many=True)
    class Meta:
        model = Class
        fields = ["date","start_time","end_time","subject","teacher","students"]
       

    def to_representation(self, instance):
        data =  super().to_representation(instance)
        sb_data = data.pop("subject")
        t_data = data.pop("teacher")
        st_data = data.pop("students")  
        del sb_data['course']
        del t_data['subjects']
        for key in st_data:
            del key["course"]     
        data.update({"Subject": sb_data})
        data.update({"Teacher" : t_data})
        data.update({"Students": st_data})
        return data
