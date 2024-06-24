from django.contrib import admin
from .models import Link, Ref, LinkRef
# Register your models here.


class LinkRefInline(admin.TabularInline):
    model = LinkRef

@admin.register(Ref)
class RefAdmin(admin.ModelAdmin):
    list_display = ('id', 'url')
    
@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    inlines = (LinkRefInline,)
    list_display = ('name', 'id',)
    search_fields = ('name',)
    