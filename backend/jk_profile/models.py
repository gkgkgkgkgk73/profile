from django.db import models

class Career(models.Model):
    name = models.CharField(max_length = 200)          
    period = models.CharField(max_length = 200)  
    description = models.JSONField()
    role = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length = 200)
    picture= models.JSONField()
    description = models.CharField(max_length = 200)
    fetool = models.CharField(max_length = 200)
    betool = models.CharField(max_length = 200)
    role = models.CharField(max_length = 200)
    period = models.CharField(max_length = 200)
    gain = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name
