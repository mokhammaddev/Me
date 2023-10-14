from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=221)
    email = models.EmailField(unique=True, null=True, blank=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
