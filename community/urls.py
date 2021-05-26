from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.reviews, name ='reviews'), # 리뷰 전체 페이지
    path('<int:review_id>/',views.review_detail, name='review_detail'), # 단일 리뷰 페이지 
    path('<int:movie_id>/review/',views.review_craeted, name='review_craeted'), # 리뷰 생성 
    path('review/<int:review_id>/delete/',views.review_delete, name='review_delete'), # 리뷰 삭제 

    path('<int:review_id>/comment/',views.comment_create, name='comment_create'), # 댓글 생성 
    path('comment/<int:comment_id>/delete/',views.comment_delete, name='comment_delete'), # 댓글 삭제 

    path('<int:review_id>/like/',views.like, name='like'), # 좋아요 버튼 
    path('<int:review_id>/funny/',views.funny, name='funny'),# 재밌어요 버튼 
    path('<int:review_id>/helpful/',views.helpful, name='helpful'), # 도움이 됬어요 버튼 
    path('<int:comment_id>/comment/like/',views.comment_like, name='comment_like') # 댓글의 좋아요 버튼 
] 
