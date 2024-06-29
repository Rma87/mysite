from django.db import models


class Post(models.Model):
    # image
    # author
    title = models.CharField(max_length=200)
    content = models.TextField()
    # tag 
    # category
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateField(null=True)
    published_time = models.TimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']
    
    def __str__(self) -> str:
        return " {} - {} ".format(self.titele, self.id)