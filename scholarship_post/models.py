from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

#scholarship_blog model post
class ScholarshipPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    eligibility_criteria = models.TextField()
    dead_line = models.DateField(default=timezone.now)
    link = models.URLField(blank=True, max_length=255, null=True)
    created_at = models.DateField(default=timezone.now)
    created_by = models.ForeignKey(User, related_name="scholarships", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
#scholarship_blog model contact us
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    message = models.TextField()
    
    def __str__(self):
        return self.name