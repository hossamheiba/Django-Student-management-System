from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Students(models.Model):
    STUDENTS_CLASS = (
        ('10 a','10 a'),
        ('10 b','10 b'),
    )
    
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 150)
    student_class=models.CharField(choices=STUDENTS_CLASS, max_length=50)
    mobile_number=models.CharField(max_length=10)
    address = models.CharField(max_length = 150)
    img=models.ImageField(upload_to='image_student')
    slug=models.SlugField(blank=True ,null=True)

    
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Students,self).save(*args,**kwargs)
 
    
    def __str__(self):
        return self.name

