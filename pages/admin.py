from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site
from .models import *



@admin.register(AboutUsPage)
class AboutUsPageAdmin(admin.ModelAdmin):
    list_display = ['__str__']

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'role']

    def has_add_permission(self, request):
        if self.model.objects.count() >= 20:
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(SEOMeta)
class SEOMetaAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    
@admin.register(BlogHeader)
class BlogHeaderAdmin(admin.ModelAdmin):
    list_display = ['__str__']

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(HomeHeader)
class HomeHeaderAdmin(admin.ModelAdmin):
    list_display = ['__str__']

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(SocialHeader)
class SocialHeaderAdmin(admin.ModelAdmin):
    list_display = ['__str__']

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False

        
@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    
    def has_add_permission(self, request):
        return False

    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    
    def has_add_permission(self, request):
        return False

    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]


#admin.site.unregister(FlatPage)
#@admin.register(FlatPage)
#class FlatPageAdmin(admin.ModelAdmin):
#    
#    def has_add_permission(self, request):
#        if self.model.objects.count() >= 3:
#            return False
#        return super().has_add_permission(request)
#
#    def has_delete_permission(self, request, obj=None):
#        return False


admin.site.unregister(Site)
class SiteAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'domain')
    readonly_fields = ('id',)
    list_display = ('id', 'name', 'domain')
    list_display_links = ('name',)
    search_fields = ('name', 'domain')
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
admin.site.register(Site, SiteAdmin)
