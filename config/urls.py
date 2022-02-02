from argparse import Namespace
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('board.urls')),
    path('', include('board_form.urls')),
    path('', include('album.urls')),
]
