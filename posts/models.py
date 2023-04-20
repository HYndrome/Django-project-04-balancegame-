from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    select1_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='selects1')
    select1_content = models.CharField(max_length=50)
    select2_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='selects2')
    select2_content = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def image_path(instance, filename):
        return f'posts/{instance.pk}/{filename}'
    image1 = models.ImageField(upload_to=image_path, blank=True, null=True)
    image2 = models.ImageField(upload_to=image_path, blank=True, null=True)
