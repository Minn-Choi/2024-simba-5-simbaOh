from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = "main"
urlpatterns = [
    path('', intro, name='intro'),
    path('first-screen', first_screen, name='first_screen'),
    path('mainpage', mainpage, name='mainpage'),
    path('mentor-start', mentor_start, name='mentor-start'),
    path('mentor-list', mentor_list, name='mentor-list'),
    path('mentor-info/<int:id>', mentor_info, name='mentor-info'),
    path('mentor-enroll', mentor_enroll, name='mentor-enroll'),
    path('mentor-creat', mentor_creat, name="mentor-creat"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)