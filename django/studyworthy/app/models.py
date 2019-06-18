from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField('date published')


class Student(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(default='', max_length=200)
    email = models.CharField(max_length=200)

    def is_email_hidden(self):
        return self.email == 'hidden'


class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
