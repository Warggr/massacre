from django.views.generic import ListView, DetailView
from accounts.models import User

class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'

class UserDetailView(DetailView):
    model = User
    template_name = 'users/user_detail.html'
