from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_list(request):
	posts = Post.objects.filter(publicado_em__lte=timezone.now()).order_by('publicado_em')
	return render(request, 'blogpost/post_list.html', {'posts':posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blogpost/post_detail.html', {'post':post})

def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.autor = request.user
			post.save()
			return redirect('blogpost.views.post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blogpost/post_edit.html', {'form':form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.autor = request.user
			post.publicado_em = timezone.now()
			post.save()
			return redirect('blogpost.views.post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request,'blogpost/post_edit.html', {'form':form})

def post_draft_list(request):
	posts = Post.objects.filter(publicado_em__isnull=True).order_by('criado_em')
	return render(request, 'blogpost/post_draft_list.html', {'posts':posts})

def post_publicar(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.publicar()
	return redirect('blogpost.views.post_detail', pk=pk)

def post_remove(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	return redirect('blogpost.views.post_list')
