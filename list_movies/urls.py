from django.urls import path
from list_movies.views import show_all_movie_review, show_all_movie_details, like_view


app_name = 'list'

urlpatterns = [
    path('', show_all_movie_review, name='all'),
    path('details/<int:pk>', show_all_movie_details, name='details'),
    path('like/<int:pk>', like_view, name='like')
]