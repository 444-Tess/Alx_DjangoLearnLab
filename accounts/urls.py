from django.urls import path
from .views import RegisterView, LoginView, ProfileView, FollowViewSet

follow_list = FollowViewSet.as_view({
    'post': 'follow',
    'delete': 'unfollow'
})

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:pk>/', FollowViewSet.as_view({'post': 'follow'}), name='follow'),
    path('unfollow/<int:pk>/', FollowViewSet.as_view({'post': 'unfollow'}), name='unfollow'),
]
