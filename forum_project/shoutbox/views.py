from django.shortcuts import render
from shoutbox.models import Post
from shoutbox.forms import PostForm

def index(request):
	post_list = Post.objects.order_by('-datetime')
	context_dict = {'posts':post_list}

	return render(request,'shoutbox/index.html',context_dict)

