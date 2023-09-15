from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

# from polls import views
from polls import apiviews


router = DefaultRouter()
router.register('polls', apiviews.PollViewSet, basename='polls')

urlpatterns = [
    # path("polls/", apiviews.PollList.as_view(), name='polls_list'),
    # path("polls/<int:pk>/", apiviews.PollDetail.as_view(), name='polls_detail'),
    path("users/", apiviews.UserCreate.as_view(), name='user_create'),
    path("login/", apiviews.LoginView.as_view(), name="login"),
    # path("get-token/", views.obtain_auth_token, name="login"),
    path("polls/<int:pk>/choices/", apiviews.ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", apiviews.CreateVote.as_view(), name="create_vote"),
]

urlpatterns += router.urls