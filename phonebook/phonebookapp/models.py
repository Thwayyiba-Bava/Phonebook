from django.db import models

class Phonebook(models.Model):
    name=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

   


