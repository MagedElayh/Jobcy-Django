from django.urls import path
# urls.py
from blog import views
urlpatterns = [
    path('blog', views.Blog.as_view(),name="blog"),
    path('blog-grid', views.BlogGrid.as_view(),name="blog-grid"),
    path('blog-modern', views.BlogModern.as_view(),name="blog-modern"),
    path('blog-masonry', views.BlogMasonry.as_view(),name="blog-masonry"),
    path('blog-details', views.BlogDetails.as_view(),name="blog-details"),
    path('blog-author', views.BlogAuthor.as_view(),name="blog-author"),
]