from django.shortcuts import render
import json
from .models import StudentFeedback
from django.http import HttpResponse

def home(request):

    if request.method == "POST":
        payload = json.loads(request.body)

        feedback_type = payload.get('type')
        subject = payload.get('subject')
        message = payload.get('message')
        anonymous = payload.get('anonymous')
        name = payload.get('name')
        matric_number = payload.get('matric')

        feedback = StudentFeedback.objects.create(
            type = feedback_type,
            subject = subject,
            message = message,
            anonymous_message = anonymous
        )

        if name:
            feedback.student_name = name

        if matric_number:
            feedback.student_matric_number = matric_number

        feedback.save()
        return HttpResponse(status=200)

    return render(request, 'index.html')