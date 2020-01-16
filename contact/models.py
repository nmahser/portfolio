from django.db import models


class Contact (models.Model):

    from_email = models.EmailField(max_length=50, blank=False, default='NULL')
    subject = models.CharField(max_length=50, blank=False, default='NULL')
    message = models.TextField(blank=False, default='NULL')

    def __str__(self):
        return self.from_email
