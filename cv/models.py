from django.db import models
import uuid
# Create your models here.
class Course(models.Model):
    course_id = models.CharField(
        max_length=100, blank=True, unique=True, default=uuid.uuid4
    )
    title = models.CharField(max_length=200)
    grade = models.CharField(max_length=200)
    year_choices = (("year1", "Year 1"), ("year2", "Year 2"), ("year3", "Year 3"), ("year4", "Year 4"), ("other", "Other"))

    year = models.CharField(
        choices=year_choices, max_length=20, default="other"
    )

    def __str__(self):
        return self.title

class Skills(models.Model):
    skill_id = models.CharField(
        max_length=100, blank=True, unique=True, default=uuid.uuid4
    )
    title = models.CharField(max_length=200)
    description = models.TextField(default=None)
    experience = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Languages(models.Model):
    lang_id = models.CharField(
        max_length=100, blank=True, unique=True, default=uuid.uuid4
    )
    title = models.CharField(max_length=200)
    experience = models.CharField(max_length=20)

    def __str__(self):
        return self.title


        
