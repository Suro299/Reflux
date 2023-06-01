from django.db import models

# Create your models here.


class User_Info(models.Model):

    name = models.CharField('User name', max_length=50)
    proff = models.CharField('User proff', max_length=60)
    img = models.ImageField('User image', upload_to='images')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'User_Info'
        verbose_name_plural = 'Users_Info'

class AboutMe(models.Model):
    name = models.CharField('About name', max_length=50)
    about_text = models.TextField('About text')

    def __str__(self):
        return self.name
    
class Content(models.Model):
    name = models.CharField('Content name', max_length=50)
    text = models.TextField('Content text')
    img = models.ImageField('Content image', upload_to='images')
    button_name = models.CharField('Content button name', max_length=20)

    def __str__(self):
        return self.name
    

class Whats(models.Model):
    name = models.CharField('Whats name', max_length=50)
    whats_text = models.TextField('Whats text')

    def __str__(self):
        return self.name
    

class Skill(models.Model):
    name = models.CharField('Skill name', max_length=50)
    text = models.TextField('Skill text')
    img = models.ImageField('Skill image', upload_to='images')

    def __str__(self):
        return self.name
    

class Image_Protfolio(models.Model):

    name1 = models.CharField('Image name1', max_length=20)
    name2 = models.CharField('Image name2', max_length=20)
    img = models.ImageField('Image', upload_to='images')

    def __str__(self):
        return self.name1
    

class Contact(models.Model):
    
    name = models.CharField('Contact name', max_length=50)
    email = models.EmailField('Contact email')
    subject = models.CharField('Contact subject', max_length=200)
    message = models.TextField('Contact message')

    def __str__(self):
        return self.name