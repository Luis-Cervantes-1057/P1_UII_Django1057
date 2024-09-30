from django.urls import path 
from . import views
urlpatterns = [
    path('', view.hola, name="cervantesclase_app")
]
