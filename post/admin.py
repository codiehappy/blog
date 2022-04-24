from django.contrib import admin
from django.contrib.auth.models import User
admin.site.site_header = 'My Blog'                    # default: "Django Administration"
admin.site.index_title = 'Admin Panel'                 # default: "Site administration"
admin.site.site_title = 'adminsitration'

# Register your models here.
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image', 'author', 'date']
    list_filter = ['date', 'author__username', 'category__name']
    search_fields = ['title', 'author__username', 'category__name']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)