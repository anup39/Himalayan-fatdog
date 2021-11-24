# -*- coding: utf-8 -*-
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from django.db import models
from django.urls import reverse

from django.db.models import Q
from django.db.models.signals import pre_save

from datetime import time
from django.utils.timezone import make_aware
from time import sleep
import datetime

from Himalaya_treks_nepal.utils import  unique_slug_generator




class Category(models.Model):
    name         = models.CharField('name',max_length=200, db_index=True)
    image        = models.ImageField('header image' ,upload_to='categories/', blank=True, null=True)
    header_title = models.CharField('header title',max_length=200, blank=True, null=True)
    slug         = models.SlugField(help_text='will be generated automatically if left blank',max_length=200, db_index=True, blank=True, unique=True)

    class Meta:
        index_together = (('id', 'slug'),)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
         return reverse('blog:posts_by_category', args=[self.slug])


class PostQuerySet(models.query.QuerySet):
    def show(self):
        return self.filter(show=True)
    def search(self, query):
        lookups =  (
        			   Q(name__icontains=query) |
        			   Q(category__name__icontains=query)
        		   )
        return self.filter(lookups).distinct()


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().show()

    def search(self, query):
        return self.get_queryset().show().search(query)


class Post(models.Model):
    #user             = models.ForeignKey(User , verbose_name=_("user"), on_delete=models.SET_NULL, null=True, blank=True)
    name             = models.CharField('title', max_length=120, db_index=True)
    slug             = models.SlugField(help_text='will be generated automatically if left blank', max_length=200, db_index=True, blank=True, unique=True)
    category         = models.ForeignKey(Category, verbose_name="category", on_delete=models.CASCADE)
    image            = models.ImageField('image' ,upload_to='posts/%Y/%m/%d', blank=True, null=True)
    show             = models.BooleanField('show', default=True)
    featured         = models.BooleanField('featured',help_text='show this post on homepage ?', default=False)
    meta_tag         = models.CharField('SEO Meta Tag', max_length=120,blank=True, null=True)
    brief            = models.CharField('small brief',max_length=120,blank=True, null=True)
    content          = RichTextUploadingField('content')
    image2           = models.ImageField('image2' ,upload_to='posts/%Y/%m/%d', blank=True, null=True)
    created_at       = models.DateTimeField('created at',auto_now_add=True)
    updated_at       = models.DateTimeField('updated at', auto_now=True)

    objects = PostManager()

    class Meta:
        index_together = (('id', 'slug'),)
        ordering = ('-updated_at',)
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])


class SocialQuerySet(models.query.QuerySet):
    def show(self):
        return self.filter(show=True)


class SocialManager(models.Manager):
    def get_queryset(self):
        return SocialQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().show()

class Social(models.Model):
    name             = models.CharField('title', max_length=120, db_index=True)
    slug             = models.SlugField(help_text='will be generated automatically if left blank', max_length=200, db_index=True, blank=True, unique=True)
    image            = models.ImageField('image' ,upload_to='posts/%Y/%m/%d', blank=True, null=True)
    show             = models.BooleanField('show', default=True)
    brief            = models.CharField('small brief',max_length=120,blank=True, null=True)
    content          = RichTextUploadingField('content')
    created_at       = models.DateTimeField('created at',auto_now_add=True)
    updated_at       = models.DateTimeField('updated at', auto_now=True)

    objects = SocialManager()

    class Meta:
        index_together = (('id', 'slug'),)
        ordering = ('-updated_at',)
        verbose_name = 'Social work'
        verbose_name_plural = 'Social work'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:social_detail', args=[self.slug])




def slug_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_pre_save_receiver, sender=Category)
pre_save.connect(slug_pre_save_receiver, sender=Post)
pre_save.connect(slug_pre_save_receiver, sender=Social)
