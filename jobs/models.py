from django.db import models


class Job(models.Model):
    gif = models.ImageField(upload_to='gifs/', default='NA')
    image = models.ImageField(upload_to='images/')
    #icon = models.ImageField(upload_to='icons/', default='NA')
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=800)
    tools = models.CharField(max_length=200)
    github = models.CharField(max_length=100, default='NA')

    def __str__(self):
        return self.summary
