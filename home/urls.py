from django.urls import path
from . import views

app_name="home"

urlpatterns = [
    path("",views.home_page,name="home_page"),
    path('students/' , views.students_information , name= 'students') ,
    path("students_create/" , views.students_create, name= 'students_create') ,
    
    path("students_detail/<str:slug>" , views.students_details, name= 'students_detail') ,
    path("students_delete/<str:slug>" , views.students_delete, name= 'students_delete') ,
    path('edit/<str:slug>' , views.students_edit , name= 'student_edit') ,

] 