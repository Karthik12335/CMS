from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    

class Subject(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=50)
    student_id = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    employee_id = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50)
    subjects = models.ManyToManyField(Subject)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
