from django.contrib import admin
from .models import Categories, Post, Author
# Register your models here.


class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('cat_title',)}

admin.site.register(Categories, CategoriesAdmin)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('post_content',)}
 
admin.site.register(Post,PostAdmin )  
 
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('author_name',)}

admin.site.register(Author, AuthorAdmin)
























