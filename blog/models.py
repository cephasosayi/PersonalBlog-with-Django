from django.db import models
from django.urls import reverse
from django.utils.timezone import now
# Create your models here.
class Category(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a post category (e.g. travel)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Article(models.Model):
	title = models.CharField(max_length=200, null=False)
	description = models.TextField(max_length=1000, help_text='Enter your post content here')
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null = True)
	category = models.ManyToManyField(Category )
	photo = models.ImageField(upload_to='article_photo', null=True)
	post_date = models.DateTimeField(default=now, editable=False)
	
	def display_genre(self):
		return ', '.join(category.name for category in self.category.all()[:3])
	display_genre.short_description = 'Category'
	class Meta:
		ordering = ['post_date']

	def __str__(self):
		return f'{self.title} ({self.author.first_name})'
	def get_absolute_url(self):
		return reverse('blog-detail', args=[str(self.id)])


class Author(models.Model):
	first_name =  models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	bio = models.TextField(max_length=1000)

	class Meta:
		ordering = ['last_name', 'first_name']

	
	def __str__(self):
		return f'{self.first_name},{ self.last_name}'	
	def get_absolute_url(self):
		return reverse('author-detail', args=[str(self.id)])
