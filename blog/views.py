from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import Post, Category, Social
def home_page(request):
    featured_posts = Post.objects.filter(featured=True)
    context ={
        'featured_posts':featured_posts,
        'header':'header',
    }
    return render(request, 'home.html', context)



class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = "blog/posts.html"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['header'] = 'header'
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class SocialListView(ListView):
    model = Social
    context_object_name = 'socials'
    template_name = "blog/socials.html"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(SocialListView, self).get_context_data(**kwargs)
        context['header'] = 'header'
        return context

class SocialDetailView(DetailView):
    model = Social
    template_name = 'blog/social_detail.html'
    context_object_name = 'social'


class PostCategory(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/category.html'
    paginate_by = 4

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.filter(category=self.category,show=True)

    def get_context_data(self, **kwargs):
        context = super(PostCategory, self).get_context_data(**kwargs)
        context['category'] = self.category
        context['header'] = 'header'
        return context



class SearchPostView(ListView):
    model = Post
    context_object_name = 'results'
    template_name = "blog/search/results.html"
    paginate_by = 4

    def get_context_data(self, *args, **kwargs):
        context = super(SearchPostView, self).get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context
    def get_queryset(self):
        query = self.request.GET.get('q', None)
        if query is not None:
            return Post.objects.search(query)
        return Post.objects.none()
