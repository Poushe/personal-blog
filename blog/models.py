from django.db import models
import uuid

class author(models.Model):
    aname=models.CharField(max_length=200, null=True, blank=True)
    address=models.TextField(max_length=500, null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    def __str__(self):
        return self.aname
class blog(models.Model):
    title=models.CharField(max_length=200, null=True, blank=True)
    description=models.TextField(max_length=500, null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    conauthor=models.ForeignKey(author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
