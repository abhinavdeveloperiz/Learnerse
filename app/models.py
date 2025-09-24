from django.db import models

class Courses(models.Model):
    image = models.ImageField(upload_to='course_images/')
    name = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.name  # Changed from title to name
    
    class Meta:
        verbose_name_plural = "Courses"

class Instructor(models.Model):
    image = models.ImageField(upload_to='instructor_images/')
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.name  # Changed from title to name

class SuccessStories(models.Model):
    image = models.ImageField(upload_to='success_images/')
    name = models.CharField(max_length=200)
    story = models.TextField()

    def __str__(self):
        return self.name  # Changed from title to name
    
    class Meta:
        verbose_name_plural = "Success Stories"


        