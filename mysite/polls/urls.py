from django.urls import path

from . import views

app_name = 'polls'

# urlpatterns = [
#     path('', views.index, name = 'index'),
#     path('<int:question_id>/', views.detail, name = 'detail'),
#     path('<int:question_id>/results/', views.results, name = 'results'),
#     path('<int:question_id>/vote/', views.vote, name = 'vote')
# ]

# Amend URLconf
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name = 'results'),
    path('<int:question_id>/vote/', views.vote, name = 'vote')
]

'''Note that the name of the matched pattern in the path strings of the second and third patterns 
has changed from <question_id> to <pk>. This is necessary because we’ll use the DetailView 
generic view to replace our detail() and results() views, and it expects the primary key value 
captured from the URL to be called "pk".'''