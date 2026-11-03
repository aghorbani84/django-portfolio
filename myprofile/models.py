from django.db import models


class Experience(models.Model):
    title = models.CharField(max_length=120)
    company = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ("-start_date",)

    def __str__(self):
        return f"{self.title} — {self.company}"


class Project(models.Model):
    title = models.CharField(max_length=120)
    summary = models.CharField(max_length=240)
    description = models.TextField(blank=True)
    technologies = models.CharField(max_length=240, blank=True, help_text="Comma-separated technologies")
    repository_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-featured", "-created_at")

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=160, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.name} — {self.created_at:%Y-%m-%d}"
