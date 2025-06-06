from django.shortcuts import render
from django.http import JsonResponse
from .models import Message

def messages_view(request):
    messages = Message.objects.all().values('id', 'text')
    return JsonResponse(list(messages), safe=False)
