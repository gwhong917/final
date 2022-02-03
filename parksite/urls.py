from django.urls import path, include
from . import views

app_name = 'parksite'

urlpatterns = [
    path('dashboard.html', views.dashboard),
    path('icons.html', views.icons),
    path('map.html', views.map),
    path('notifications.html', views.notifications),
    path('tables.html', views.tables),
    path('user.html', views.user),
    # path('index/', views.index, name='index'),
]
