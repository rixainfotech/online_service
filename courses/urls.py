from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course-list'),
    path('enroll/<int:course_id>/', views.enroll, name='enroll'),
]


