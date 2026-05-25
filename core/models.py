from django.db import models


class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)
    start_date = models.CharField(max_length=20)
    end_date = models.CharField(max_length=20, default='Present')
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} @ {self.company}"


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('lang', 'Languages'),
        ('framework', 'Frameworks'),
        ('tool', 'Tools & Platforms'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='lang')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['category', 'order']

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(blank=True)
    tags = models.CharField(max_length=300, blank=True, help_text='Comma-separated tags')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def tag_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field = models.CharField(max_length=200)
    start_year = models.CharField(max_length=10)
    end_year = models.CharField(max_length=10)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.degree} @ {self.institution}"


class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ('linkedin', 'LinkedIn'),
        ('youtube', 'YouTube'),
        ('github', 'GitHub'),
        ('twitter', 'Twitter/X'),
        ('other', 'Other'),
    ]
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()
    label = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.platform}: {self.url}"
