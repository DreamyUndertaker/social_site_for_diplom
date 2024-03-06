# messenger/urls.py
from django.urls import path
from .views import ChatListView, ChatDetailView, CreateDialogView

urlpatterns = [
    path('', ChatListView.as_view(), name='chat-list'),
    path('<int:chat_id>/', ChatDetailView.as_view(), name='chat-detail'),
    path('create_dialog/', CreateDialogView.as_view(), name='create-dialog'),
]
