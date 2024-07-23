from django.shortcuts import render, get_object_or_404
from .models import Request
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'itreporting/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'itreporting/about.html', {'title': 'About'})

def contact(request):
    return render(request, 'itreporting/contact.html', {'title': 'Contact'})

def requests(request):
    daily_report = {'requests': Request.objects.all(), 'title': 'Requests Made'}
    return render(request, 'itreporting/requests.html', daily_report)

class PostListView(ListView):
    model = Request
    template_name = 'itreporting/requests.html'
    context_object_name = 'requests'
    ordering = ['-date_submitted']
    paginate_by = 10

class PostDetailView(DetailView):
    model = Request

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Request
    fields = ['type', 'game', 'details']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Request
    fields = ['type', 'game', 'details']
    def test_func(self):
        issue = self.get_object()
        return self.request.user == issue.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Request
    success_url = '/requests'
    def test_func(self):
        issue = self.get_object()
        return self.request.user == issue.author
    
