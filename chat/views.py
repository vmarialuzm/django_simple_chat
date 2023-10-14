from django.shortcuts import render, redirect
from .models import Channel, Message
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def chat_room(request, channel_id):
    channel = Channel.objects.get(id=channel_id)
    messages = Message.objects.filter(channel=channel)
    if request.method == 'POST':
        content = request.POST['content']
        Message.objects.create(channel=channel, user=request.user, content=content)
        return redirect('chat_room', channel_id=channel.id)
    return render(request, 'chat/chat_room.html', {'channel': channel, 'messages': messages})

@login_required
def create_channel(request, user_id):
    user = User.objects.get(id=user_id)
    if request.user == user:
        return redirect('index')
    channel = Channel.objects.create()
    channel.users.add(request.user, user) #se usa add porque user con channel es una relacion many to many
    return redirect('chat_room', channel_id=channel.id)
    
