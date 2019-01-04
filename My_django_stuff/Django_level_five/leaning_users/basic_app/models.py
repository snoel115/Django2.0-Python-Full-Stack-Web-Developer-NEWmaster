from django.db import models

# snoel import the model
from django.contrib.auth.models import User
# Create your models here.

# snoel create the class
class UserProfileInfo(models.Model):
    # snoel extend the User model
    user = models.OneToOneField(User, on_delete=None)

    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
