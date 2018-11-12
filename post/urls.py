from django.urls import path
from . import views

app_name = "images"
urlpatterns = [
    path(
        "", view=views.AllPost.as_view(),name="all_post"
    ),
]
