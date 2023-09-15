from django.urls import path
from polls import views

urlpatterns = [
    path("polls/", views.polls_list),
    path("polls/<int:pk>/", views.polls_detail),
]