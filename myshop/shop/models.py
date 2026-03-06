from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class ContactForm(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    subject = models.CharField(max_length=120)
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class FilesAdmin(models.Model):
    adminupload = models.FileField(upload_to="media")

    def __str__(self):
        return str(self.adminupload)


class File(models.Model):
    pdf_file = models.FileField(upload_to="media/Catalogue")

    def __str__(self):
        return str(self.pdf_file)


STATUS = ((0, "Draft"), (1, "Publish"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
