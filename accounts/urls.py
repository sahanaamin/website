from django.urls import path

from . import views

urlpatterns = [
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("contact", views.contact, name="contact"),
    path("register", views.register, name="register"),
    path("login",views.login, name="login"),
     path("signin",views.signin, name="signin"),
    path("logout",views.logout,name="logout")
]