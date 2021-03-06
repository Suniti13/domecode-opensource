from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    description = RichTextField()
    category = models.CharField(max_length=50)
    github_Repo_Link = models.CharField(null=True, blank=True, max_length=80)
    producthunt = models.CharField(null=True, blank=True, max_length=80)
    youtube_videoid = models.CharField(null=True, blank=True, max_length=11)
    linkedin = models.CharField(null=True, blank=True, max_length=100)
    demo = models.CharField(null=True, blank=True, max_length=256)
    contributors = models.TextField()
    isreleased = models.BooleanField(default=False)
    documentation_Users_Link = models.CharField(null=True,
                                                blank=True,
                                                max_length=256)
    documentation_Devs_Link = models.CharField(null=True,
                                               blank=True,
                                               max_length=256)
    slug = models.SlugField(null=True, unique=True, max_length=256)
    additional_File = models.FileField(
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(allowed_extensions=[
                "pdf", "pptx", "ppt", "md", "txt", "jpeg", "png"
            ])
        ],
        upload_to="media",
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("creator:detail", kwargs={"slug": self.slug})
