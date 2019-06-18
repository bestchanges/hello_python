from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from app.models import Course


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def course_info(request, course_id):
    course = Course.objects.get(id=course_id)
    return HttpResponse(f"course_info {course.title}")