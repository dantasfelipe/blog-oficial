from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
	posts = Post.objects.filter(publicado_em__lte=timezone.now()).order_by('publicado_em')
	return render(request, 'blogpost/post_list.html', {'posts':posts})

