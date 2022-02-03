from django.shortcuts import render, redirect
from django.http import HttpResponse

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
    return render(request, "tables.html")


def user(request):
    return render(request, "user.html")



