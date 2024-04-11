from django.urls import path
from . import views

app_name = 'materials'
urlpatterns = [
    path('materials/', views.materials, name='materials'),
    path('download-book/<int:pk>', views.downloadBook, name='downloadBook')
]
