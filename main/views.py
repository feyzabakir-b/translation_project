# main/views.py

from django.shortcuts import render
from django.db.models import Q
from rest_framework import viewsets
from .models import City
from .serializers import CitySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from unidecode import unidecode
from django.utils.translation import gettext as _

def home(request):
    return render(request, 'home.html')

def city_list(request):
    search_query = request.GET.get('search', '')
    cities = City.objects.all()
    
    if search_query:
        normalized_query = unidecode(search_query.lower())
        cities = cities.filter(
            Q(normalized_name__icontains=normalized_query) |
            Q(description__icontains=search_query)
        )
    
    return render(request, 'city_list.html', {'cities': cities})

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['normalized_name', 'description']

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            normalized_query = unidecode(search_query.lower())
            queryset = queryset.filter(
                Q(normalized_name__icontains=normalized_query) |
                Q(description__icontains=search_query)
            )
        return queryset