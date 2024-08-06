from django.urls import path
from lettings import views

app_name = "lettings"
urlpatterns = [
    path("lettings/", views.index, name="lettings_index"),
    path("lettings/<letting_id>/", views.letting, name="letting"),
]
