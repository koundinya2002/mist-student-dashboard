from django.urls import path
from . import views

urlpatterns = [
    path("<str:class_id>/", views.index, name="classwork"),
    path("<str:class_id>/classwork/new/", views.post_assignment, name="post_assignment"),
    # path("<str:class_id>/classmates/", views.classmates, name="classmates")
    
]