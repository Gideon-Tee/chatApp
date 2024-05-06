from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'chatapp/index.html')


def check_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        room_name = request.POST['room_name']

        if Room.objects.filter(name=room_name).exists():
            # return redirect('chatroom', room_name)
            return redirect(f'/{room_name}/?username={username}')
        else:
            room = Room.objects.create(name = room_name)
            room.save()
            # return redirect('chatroom', room_name)
            return redirect(f'/{room_name}/?username={username}')

    else:
        return render(request, 'chatapp/index.html')

def chatroom(request, room_name):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room_name)

    context = {
        'room_name': room_name,
        'room_details': room_details,
        'username': username
    }
    return render(request, 'chatapp/chatroom.html', context)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(text=message, user=username, room=room_id)
    new_message.save()

    return HttpResponse('message sent successfully')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})
