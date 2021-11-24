from django.urls import path
from . import views
from blog.sitemaps import PostSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps={
    'posts':PostSitemap,
}

app_name = 'blog'

urlpatterns = [
    path('', views.home_page , name='home' ),
    path('search/', views.SearchPostView.as_view() , name='search' ),
    path('posts/', views.PostListView.as_view() , name='posts' ),
    path('post/<slug>/', views.PostDetailView.as_view() , name='post_detail' ),
    path('socials/', views.SocialListView.as_view() , name='socials' ),
    path('social/<slug>/', views.SocialDetailView.as_view() , name='social_detail' ),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('<slug>/', views.PostCategory.as_view() , name='posts_by_category' ),

]

