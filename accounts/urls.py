from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token
app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),  # 회원가입 
    path('login/', obtain_jwt_token), # login jwt 토큰 발급
    path('<str:username>/', views.profile, name='profile'), # 마이페이지 url 
    path('follow/<str:username>/', views.follow, name='follow'), # 유저 팔로우  
]
