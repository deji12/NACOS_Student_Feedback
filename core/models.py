from django.db import models

class StudentFeedback(models.Model):

    type = models.CharField(max_length=20, help_text="The type of feedback this is")
    subject = models.CharField(max_length=100, help_text="The subject of the feedback")
    message = models.TextField(help_text="The actual message of thos feedback")
    anonymous_message = models.BooleanField(default=True, help_text="Whether the student provided their name and mat number or not")
    student_name = models.CharField(max_length=100, help_text="The student's name (optional)")
    student_matric_number = models.CharField(max_length=100, help_text="The student's mat number (optional)")
    date_added = models.DateTimeField(auto_now_add=True, help_text="The date and time this feedback was created")
    addressed = models.BooleanField(default=False, help_text="Whether a NACOS exco has reviewed this feedback")

    def __str__(self):
        return self.subject