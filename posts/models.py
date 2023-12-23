from django.db import models
from catagories.models import Catagory
from author.models import Author

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    catagory = models.ManyToManyField(Catagory) # ekta post multiple catagory te thakte pare,abr ekta catagory er moddhe multiple post thakte
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

