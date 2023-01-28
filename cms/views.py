from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets
from .models import Class,Student,Teacher,Subject,Course
from .serializers import ClassSerializer,CourseSerializer,StudentSerializer,SubjectSerializer,TeacherSerializer




class StudentView(viewsets.ViewSet):
    """
    To view all the Students
    """
    queryset = Student.objects.all().select_related("course")
    def list(self,request):
        
        serializer = StudentSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
    To add  the Students
    """
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=201)


class TeacherView(viewsets.ViewSet):
    """
    To view all the teachers 
    """
    queryset = Teacher.objects.all()
    def list(self,request):
        serializer = TeacherSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
    To add  the Teachers
    """
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            teacher = serializer.save()
            subjects = request.data.get("subjects")
            if subjects:
                for subject_id in subjects:
                    subject = Subject.objects.get(id=subject_id)
                    teacher.subjects.add(subject)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            


class CourseView(viewsets.ViewSet):
    """
    To view all the Course
    """
    queryset = Course.objects.all()
    def list(self,request):
        serializer = CourseSerializer(self.queryset, many=True)
        return Response(serializer.data)



class SubjectView(viewsets.ViewSet):
    """
    To view all the Subjects
    """
    queryset = Subject.objects.all()
    def list(self,request):
        serializer = SubjectSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ClassView(viewsets.ViewSet):
    """
    To view all the class
    """
    queryset = Class.objects.all()
    def list(self,request):
        serializer = ClassSerializer(self.queryset, many=True)
        return Response(serializer.data)
