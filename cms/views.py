from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Class,Student,Teacher,Subject,Course
from .serializers import ClassSerializer,CourseSerializer,StudentSerializer,SubjectSerializer,TeacherSerializer



class StudentView(viewsets.ViewSet):
    queryset = Student.objects.all().select_related("course")
    def list(self,request):
        
        serializer = StudentSerializer(self.queryset, many=True)
        return Response(serializer.data)




class TeacherView(viewsets.ViewSet):
    queryset = Teacher.objects.all()
    def list(self,request):
        serializer = TeacherSerializer(self.queryset, many=True)
        return Response(serializer.data)


class CourseView(viewsets.ViewSet):
    queryset = Course.objects.all()
    def list(self,request):
        serializer = CourseSerializer(self.queryset, many=True)
        return Response(serializer.data)



class SubjectView(viewsets.ViewSet):
    queryset = Subject.objects.all()
    def list(self,request):
        serializer = SubjectSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ClassView(viewsets.ViewSet):
    queryset = Class.objects.all()
    def list(self,request):
        serializer = ClassSerializer(self.queryset, many=True)
        return Response(serializer.data)
