from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from app.models import Course, Student


def index(request):
    courses = Course.objects.all()
    template = loader.get_template("courses.html")
    context = {
        'courses': courses,
    }
    return HttpResponse(template.render(context, request))

def course_info(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    template = loader.get_template("course.html")
    context = {
        'course': course,
    }
    return HttpResponse(template.render(context, request))


def enroll(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    student = Student()
    student.name = request.POST['student_name']
    student.save()
    template = loader.get_template("course.html")
    context = {
        'course': course,
    }
    return HttpResponse(template.render(context, request))
