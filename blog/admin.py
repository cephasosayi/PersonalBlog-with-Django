from django.contrib import admin

# Register your models here.
# from .models import 
from .models import Article, Author,Category

admin.site.register(Category)
admin.site.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'category')

# admin.site.register(Author)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name')
	fields = ['first_name','last_name', 'bio']

