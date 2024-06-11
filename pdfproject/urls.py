from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('front/', views.front, name='front'),# Maps the URL 'front/' to the front view function and names it 'front'
    path('split_files/', views.split_pdf, name='split_pdf'),# Maps the URL 'split_files/' to the split_pdf view function and names it 'split_pdf'
]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)# Adds URL patterns to serve media files from MEDIA_ROOT during development
