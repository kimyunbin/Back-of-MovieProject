from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.main), # 영화 메인 
    path('detail/<int:movie_pk>', views.movie_detail), # 단일 영화 
    path('tournament', views.tournament), # 영화 월드컵 
    path('mypageMovie/<str:username>', views.mypageMovie) # 영화 월드컵 우승
]
