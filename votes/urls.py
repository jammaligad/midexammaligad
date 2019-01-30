from django.urls import path
from . import views

app_name = 'votes'
urlpatterns = [
    path('', views.index, name='index'),
    path('candidate_create/', views.candidate_create, name='newcandidate'),
    path('position_create/', views.position_create, name='newposition'),
    path('<int:candidate_id>/', views.candidate_detail, name='detail'),
    path('<int:candidate_id>/update', views.candidate_update, name='update'),
    path('<int:candidate_id>/vote', views.vote, name='vote'),
]
