from  rest_framework import serializers

from .models import Class,Course,Student,Subject,Teacher

class CourseSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Course
        fields = ["id","name"]

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

    def create(self, validated_data):
        course_data = validated_data.pop('course')
        print(course_data)
        id =course_data['name']
        course = Course.objects.get(id=id)
        student = Student.objects.create(course=course, **validated_data)
        return student
    

    

class TeacherSerializer(serializers.ModelSerializer):
    subjects = serializers.SerializerMethodField()
    class Meta:
        model = Teacher
        fields = ["id","name","employee_id","email","subjects",]

    def get_subjects(self, obj):
        key = [s.id for s in obj.subjects.all()]
        value = [s.name for s in obj.subjects.all()]
        dict = {k:v for (k,v) in zip(key,value)}
        return dict


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
     
        ft_data = {k: v for k, v in t_data.items() if k in ['id', 'name']}
        data.update({"Subject": sb_data})
        data.update({"Teacher" : ft_data})
        data.update({"Students": st_data})
        return data
