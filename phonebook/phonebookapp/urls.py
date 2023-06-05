from django.urls import path
from .import views


urlpatterns = [
    path('',views.home, name='home'),
    path('Home1',views.add_contact),
    path('Home2',views.update_contact),
    path('Home3',views.display)
   


]