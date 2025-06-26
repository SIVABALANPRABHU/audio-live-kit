# call/views.py
from django.shortcuts import render
from django.http import JsonResponse
from jose import jwt
from django.conf import settings
import time

def index(request):
    return render(request, 'call/index.html')

def get_token(request):
    room_name = request.GET.get('room', 'audio-room')
    participant_name = request.GET.get('participant', 'user')
    
    token = jwt.encode(
        {
            'exp': int(time.time()) + 3600,  # Token expires in 1 hour
            'iss': settings.LIVEKIT_API_KEY,
            'sub': participant_name,
            'nbf': int(time.time()),
            'video': {
                'room': room_name,
                'roomJoin': True,
                'canPublish': True,
                'canSubscribe': True
            }
        },

        settings.LIVEKIT_API_SECRET,
        algorithm='HS256'
    )
    
    return JsonResponse({
        'token': token,
        'livekit_url': settings.LIVEKIT_URL
    })