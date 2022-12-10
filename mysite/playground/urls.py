from django.urls import path
from . import views

# URLConf
app_name = 'playground'
urlpatterns = [
    path('', views.say_hello, name='hello'),
    path('index', views.IndexView.as_view(), name='index'),
    # path('index2', views.index2, name='index2'),
    # path('index3', views.index3, name='index3'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]

