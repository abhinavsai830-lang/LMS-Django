from django.db import models


class Course(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.title
class Enrollment(models.Model):

    student = models.ForeignKey(
        "adminapp.AdminUser",
        on_delete=models.CASCADE
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.course.title}"

class Lecture(models.Model):

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)

    video_url = models.URLField(blank=True, null=True)
    material = models.FileField(upload_to="materials/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title