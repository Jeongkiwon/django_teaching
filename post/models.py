from django.db import models
# Create your models here.

class Post(models.Model):
    title = models.CharField('TITLE',max_length=50)
    description=models.CharField('DESCRIPTION',max_length=100,blank=True,help_text='simple description text.')
    content=models.TextField('CONTENT')

    create_date=models.DateTimeField('Create_Date',auto_now_add=True)
    modify_date=models.DateTimeField('Modify_Date',auto_now=True)

    def __str__(self):
        return self.title
