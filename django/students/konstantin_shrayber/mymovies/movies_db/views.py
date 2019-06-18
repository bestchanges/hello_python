# Create your views here.
from django.http import HttpResponse
from movies_db.models import *


def index(request):
    mod_insta_list = 'studio: ' + HollywoodCompany.objects.all()[0].title + '\r\n'
    mod_insta_list += 'presents: ' + Movie.objects.all()[0].title + ', ' + str(Movie.objects.all()[0].release_year) + '\r\n'
    mod_insta_list += 'from director ' + Movie.objects.all()[0].director.full_name + '\r\n'
    mod_insta_list += 'starring ' + MovieCrew.objects.all()[0].person.full_name + ' and ' + MovieCrew.objects.all()[1].person.full_name

    return HttpResponse(mod_insta_list)