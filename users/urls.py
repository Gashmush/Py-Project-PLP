from django.urls import path
from .views import login_user,logout_user,register_customer,register_worker, register_template

urlpatterns=[
    path("login/",login_user, name="login"),
    path("register/",register_template, name="register" ),
    path("register-customer/",register_customer, name="register_customer"),
    path("register-worker/",register_worker, name="register_worker"),
    path("logout/",logout_user, name="logout"),
]