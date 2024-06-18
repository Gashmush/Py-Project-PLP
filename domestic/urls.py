from django.urls import path 
from .views import worker_register_form,workers_list,worker_detail,user_dashboard,home_page

urlpatterns=[
    path("",home_page, name="home"),
    path("list/", workers_list, name="list"),
    path("register-worker-form/", worker_register_form, name="worker-register-form"),
    path("category/<slug:category_slug>/", workers_list, name="categories"),
    path("worker-detail/<slug:slug>/", worker_detail, name="detail"),
    path("dashboard/",user_dashboard, name="dashboard")
]