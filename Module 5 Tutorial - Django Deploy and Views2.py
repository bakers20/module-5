from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
]
def post_list(request):
    return render(request, 'blog/post_list.html', {})