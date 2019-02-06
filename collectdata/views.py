from django.shortcuts import render
from .forms import DatastringForm, DataSDMForm
from django.shortcuts import redirect
from django.views.generic import ListView
from .models import Datastring, DataSDM
from django.shortcuts import reverse, render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def post_data(request):
    if request.method == 'POST':
        form = DatastringForm(request.POST)
        print(request.POST)
        if form.is_valid():
            data = form.save()
    #return redirect(reverse('collectdata:get_data'))
    return HttpResponse("ESP Ok!")


@csrf_exempt
def post_data_sdm(request):
    if request.method == 'POST':
        form = DataSDMForm(request.POST)
        print(request.POST)
        if form.is_valid():
            data = form.save()
    #return redirect(reverse('collectdata:get_data'))
    return HttpResponse("SDM Ok!")


class DataList(ListView):
    model = Datastring
    template_name = 'data_list.html'
    context_object_name = 'objects'


class DataListESPLast10(ListView):
    model = Datastring
    template_name = 'data_list.html'
    context_object_name = 'objects'

    def get_queryset(self):
        qs = super(DataListESPLast10, self).get_queryset()
        print(qs.last().temp)
        return reversed(qs.order_by('-id')[:10])


class DataListSDM(ListView):
    model = DataSDM
    template_name = 'data_list_sdm.html'
    context_object_name = 'objects'

