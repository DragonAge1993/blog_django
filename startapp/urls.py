from django.urls import path
from django.views.generic import ListView,DetailView
from startapp.models import Articles
from .import views
urlpatterns = [
    path('', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20],template_name="startapp/posts.html")),
    path('<int:pk>', DetailView.as_view(model=Articles,template_name="startapp/post.html"))
]
