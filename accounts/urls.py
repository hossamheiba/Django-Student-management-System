from django.urls import path
from . import views

app_name="accounts"

urlpatterns = [
    path("signup",views.SignUp,name="signup"),
    path("profile/",views.My_Profile,name="profile"),
    path("profile/edit",views.Edit_My_Profile,name="edit_my_profile"),
    path("pass_change/",views.Change_Password,name="change_password"),
] 