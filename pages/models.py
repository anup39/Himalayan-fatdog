from django.db import models
from django.urls import reverse



class AboutUsPage(models.Model):
    first_title = models.CharField('first title',max_length=200, db_index=True)
    second_title = models.CharField('second title',max_length=200, blank=True, null=True)
    #image = models.ImageField('image' ,upload_to='pages/about/')
    content = models.TextField('content')

    class Meta:
        verbose_name = 'AboutUsPage'
        verbose_name_plural = 'AboutUsPage'

    def __str__(self):
        return self.first_title

    def get_absolute_url(self):
         return reverse('pages:about_us')


class Member(models.Model):
    name  = models.CharField('name',max_length=200)
    role  = models.CharField('role',max_length=200)
    about = models.CharField(max_length=2000, default="",blank=True, null=True)
    image = models.ImageField('image' ,upload_to='pages/about/members/', blank=True, null=True)

    class Meta:
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
         return reverse('pages:about_us')
class SEOMeta(models.Model):
    meta_tag = models.CharField('SEO Meta Tag', max_length=450)

    class Meta:
        verbose_name = 'Meta tag'
        verbose_name_plural = 'Meta tags'

    def __str__(self):
        return self.meta_tag

# class SocialWork(models.Model):
#     pass

class HomeHeader(models.Model):
    title        = models.CharField('main title',max_length=200)
    header_title = models.CharField('second title',max_length=200)
    video        = models.FileField(upload_to='header')
    

    class Meta:
        verbose_name = 'HomeHeader'
        verbose_name_plural = 'HomeHeader'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:home')

class BlogHeader(models.Model):
    title = models.CharField('main title',max_length=200)
    header_title = models.CharField('second title',max_length=200)
    image = models.ImageField('image' ,upload_to='pages/blog/')

    class Meta:
        verbose_name = 'BlogHeader'
        verbose_name_plural = 'BlogHeader'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:posts')


class SocialHeader(models.Model):
    title = models.CharField('main title',max_length=200)
    header_title = models.CharField('second title',max_length=200)
    image = models.ImageField('image' ,upload_to='pages/blog/')

    class Meta:
        verbose_name = 'SocialHeader'
        verbose_name_plural = 'SocialHeader'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:socials')


class Enquiry(models.Model):
    message = models.TextField()
    full_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    country = models.CharField(max_length=120, blank=True, null=True)
    phone = models.CharField('Contact Number',max_length=120, blank=True, null=True)


    class Meta:
        verbose_name = 'Enquiry'
        verbose_name_plural = 'Enquiries'

    def __str__(self):
        return self.email


class Booking(models.Model):
    message = models.TextField()
    package = models.CharField('Requested Package',max_length=120, blank=True, null=True)
    full_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    country = models.CharField(max_length=120, blank=True, null=True)
    phone = models.CharField('Contact Number',max_length=120, blank=True, null=True)


    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return self.email
