from django.db import models
from django.urls import reverse # new
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # redirect user to post_detail page after form submission
        # using reverse allows us to reference an object by its URL template name
        return reverse('post_detail', args=[str(self.id)])
    