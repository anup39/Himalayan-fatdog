from .models import SEOMeta, BlogHeader, HomeHeader, SocialHeader


def meta_tags(request):
    meta_tags = SEOMeta.objects.all()
    return {'meta_tags': meta_tags}


def headers(request):
    home_header = HomeHeader.objects.all().first()
    blog_header = BlogHeader.objects.all().first()
    social_header = SocialHeader.objects.all().first()
    return {
        'home_header': home_header,
        'blog_header': blog_header,
        'social_header': social_header,
        }
