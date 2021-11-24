from django.contrib.sitemaps import Sitemap
from .models import Post
 

class PostSitemap(Sitemap):
    def posts(self):
        return Post.objects.all
