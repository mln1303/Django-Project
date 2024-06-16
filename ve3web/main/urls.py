from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload, name='upload_csv'),
    path('upload/', views.upload, name='upload'),
    path('success/<str:filename>/', views.success, name='success'),
    path('file_already_uploaded/<str:filename>/', views.file_already_uploaded, name='file_already_uploaded'),
    path('first_rows/<str:filename>/', views.first_rows, name='first_rows'),
    path('statistics/<str:filename>/', views.statistics, name='statistics'),
    path('handle_missing_values/<str:filename>/', views.handle_missing_values, name='handle_missing_values'),
    path('visualize/<str:filename>/', views.visualize_data, name='visualize_data'),
]



