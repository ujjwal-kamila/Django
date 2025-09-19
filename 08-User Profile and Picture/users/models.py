from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Profile(models.Model):
    # Create a one-to-one relationship with the built-in User model
    # means Each Profile belongs to exactly ONE User
    # and each User can have at most ONE Profile.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')


    # # Example of extra fields you may want in the profile
    # bio = models.TextField(blank=True, null=True)   # Short intro/about user
    # profile_pic = models.ImageField(upload_to="profiles/", blank=True, null=True)  # Profile photo

    # When printing a Profile object, show username
    def __str__(self):
        return f"{self.user.username} Profile"
