from django.db import models

# Create your models here.
#snoel - create a class ===================================================
class Users(models.Model):
    FirstName = models.CharField(max_length=50, unique=False)
    LastName = models.CharField(max_length=50, unique=False)
    Email = models.EmailField(unique=True)

    def __str__(self):
        # return "FN: %s, LN: %s and email: %s".format(self.FirstName, self.LastName, self.Email)
        return self.FirstName + ", " + self.LastName
