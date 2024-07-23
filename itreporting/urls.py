from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'itreporting'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name ='about'),
    path('contact/', views.contact, name='contact'),
    path('requests/', PostListView.as_view(), name = 'requests'),
    path('requests/<int:pk>', PostDetailView.as_view(), name = 'request-detail'),
    path('requests/new', PostCreateView.as_view(), name = 'request-create'),
    path('requests/<int:pk>/update/', PostUpdateView.as_view(), name = 'request-update'),
    path('requests/<int:pk>/delete/', PostDeleteView.as_view(), name = 'request-delete'),
]