# messenger/views.py
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import CreateDialogForm, MessageForm
from .models import Chat, Message


@method_decorator(login_required, name='dispatch')
class ChatListView(View):
    template_name = 'messenger/chat_list.html'

    def get(self, request):
        chats = Chat.objects.filter(participants=request.user)
        return render(request, self.template_name, {'chats': chats})


@method_decorator(login_required, name='dispatch')
class ChatDetailView(View):
    template_name = 'messenger/chat_detail.html'

    def get(self, request, chat_id):
        chat = Chat.objects.get(id=chat_id)
        form = MessageForm()
        messages = chat.messages.all()  # Fetch only sent messages
        return render(request, self.template_name, {'chat': chat, 'form': form, 'messages': messages})

    def post(self, request, chat_id):
        chat = Chat.objects.get(id=chat_id)
        form = MessageForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            message = Message.objects.create(chat=chat, author=request.user, content=text)
        print("Message created:", message.content)
        return redirect('chat-detail', chat_id=chat.id)


class CreateDialogView(View):
    template_name = 'messenger/create_dialog.html'

    def get(self, request):
        form = CreateDialogForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CreateDialogForm(request.POST)
        if form.is_valid():
            participant = form.cleaned_data['participant']

            # Проверка наличия чата с участием указанных участников
            existing_chat = Chat.objects.filter(participants__in=[request.user, participant])
            if existing_chat.exists():
                return HttpResponse("Chat already exists with these participants.")

            chat = Chat.objects.create()
            chat.participants.add(request.user, participant)
            return redirect('chat-detail', chat_id=chat.id)

        return render(request, self.template_name, {'form': form}),({'form': form})
