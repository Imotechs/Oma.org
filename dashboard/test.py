from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(verbose_name="Date of Birth")
#added
    def __str__(self):
        return f"{self.user}'s profile"


class Job(models.Model):
    title = models.CharField(verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    salary = models.FloatField(default=0)
#added
    def __str__(self):
        return f"{self.title}"

   #in views.py
profiles = UserProfile.objects.all() #returns all userprofiles objects and assign to profiles

Job.objects.values('id').annotate(average_salary = Avg('salary'))#annotated with associated job ids to get the average salary

# Add any missing Django best practices to model definitions

# Please write a single queryset that will return all UserProfile objects
# annotated with associated job ids