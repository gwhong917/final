from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Test
from django.db import connection
import folium


def dashboard(request):
    return render(request, "dashboard.html")


def icons(request):
    return render(request, "icons.html")


def map(request):
    return render(request, "map.html")


def notifications(request):
    return render(request, "notifications.html")


def tables(request):

    data_table_test = Test.objects.all()
    print(type(data_table_test))

    return render(request, "tables.html", {
        'data_table_test': data_table_test
    })


def user(request):
    return render(request, "user.html")

