from django.db import models
## NOT this
# from datetime import timezone
# But This
from django.utils import timezone
from django.core.urlresolvers import reverse
# Create your models here.

class Posts(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=255)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank = True,null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def approved_comments(self):
        return self.comments.filter(approved = True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})

class Comments(models.Model):
    post = models.ForeignKey(Posts,related_name='comments')
    author = models.CharField(max_length=255)
    text = models.TextField()
    create_date = models.DateTimeField(default = timezone.now())
    published_date = models.DateTimeField(blank=True,null=True)
    approved = models.BooleanField(default=False)
    def approve_comment(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text
