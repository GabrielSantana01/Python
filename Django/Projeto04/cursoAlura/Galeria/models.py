from django.db import models

class teste01(models.Model):
    tagname =  models.CharField(max_length=50)   

    def __str__(self):
        return self.tagname
    


