from django.urls import path
from .views import (ArticleListView,
                    ArticleUpdateView, 
                    ArticleDetailView, 
                    ArticleDeleteView,
                    ArticleCreateView,
                    ArticleCommentView,
                    MyArticlesView)
                    

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('my_list/', MyArticlesView.as_view(), name='my_view'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'), 
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('<int:article_id>/comment/', ArticleCommentView.as_view(), name='add_comment'), # Commenting on the template...
    
]
