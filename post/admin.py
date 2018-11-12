from django.contrib import admin
from post.models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','modify_date','description')
    list_filter = ('modify_date',)
   
admin.site.register(Post, PostAdmin)